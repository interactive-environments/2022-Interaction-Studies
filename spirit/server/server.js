import { WebSocketServer } from 'ws';
import * as mqtt from "mqtt"
import {GUIMessageHandler} from './GUI-message-handler.js'
import * as defaultNeighbours from "./default-neighbours.js"

const mqttClient  = mqtt.connect('mqtts://greatinteractivereef.cloud.shiftr.io/', {
    clientId: "Spirit",
    username: "greatinteractivereef",
    password: "YbOk0JfBm8dtVkW3"
})
const webSocketServer = new WebSocketServer({ port: 3001 });

const PASSWORD = "InteractiveEnvironments2022"

let guis = []

const guiMessageHandler = new GUIMessageHandler(mqttClient)

if (defaultNeighbours.neighbours)
    guiMessageHandler.setNeighbours(defaultNeighbours)

//------------------------------
//------- GUI connection -------
webSocketServer.on('connection', function connection(ws) {
    ws.on('message', function message(data) {
        // Got a message from the GUI
        try {
            const dataObject = JSON.parse(data.toString())

            // Check if the GUI has the correct password
            if (typeof dataObject === "undefined"|| typeof dataObject.password === "undefined" || dataObject.password !== PASSWORD)
                ws.send(JSON.stringify({error: "Invalid Credentials"}))

            // Handle the message
            console.log(dataObject)
            switch (dataObject.messageType) {
                case "changeDayNight":
                    guiMessageHandler.changeDayNight(dataObject)
                    break;
                case "updateInterval":
                    guiMessageHandler.changeTimePulse(dataObject)
                    break
                case "setNeighbours":
                    guiMessageHandler.setNeighbours(dataObject)
                    break;
            }
        } catch (e) {
            console.error(e)
        }

    });

    ws.send(JSON.stringify({message: "connected!"}));

    ws.on("close", () => {
	guis = guis.filter(x => x !== ws)
    })

    guis.push(ws)

    // Send neighbour data
    guiMessageHandler.sendNeighbours(guis)
});

//------------ MQTT Connection

mqttClient.on('connect', function () {
//    mqttClient.subscribe('presence', function (err) {
    //      if (!err) {
    //        mqttClient.publish('presence', 'Hello mqtt')
    //  }
    //})

    // Subscribe to energy level
    mqttClient.subscribe('energy-level')
    mqttClient.subscribe('names')

    // Time pulse
    guiMessageHandler.timePulseInterval = setInterval(sendTimePulse, guiMessageHandler.timePulse * 1000)


    // Day night message
    guiMessageHandler.timeOfDayInterval = setInterval(sendDayNight, guiMessageHandler.timeOfDayIntervalTime * 1000)


    // Clear all timers
    mqttClient.on("disconnect", ()=> {
        clearInterval(guiMessageHandler.timePulseInterval)
        clearInterval(guiMessageHandler.timeOfDayInterval)
    })
})


mqttClient.on('message', function (topic, message) {
    const text = message.toString()
    // message is Buffer
    switch(topic) {
	case "energy-level":
	    const data = text.split(", ")
	    //console.log(data)
	    guiMessageHandler.changeCreatureEnergy(data[0],data[1],guis, mqttClient)
	    break;
    case "names":
        guiMessageHandler.getName(text, guis)
        break;
    }
})

// Give a time pulse with a value the time till the next pulse
let previousTimePulse = guiMessageHandler.timePulse
function sendTimePulse() {
    if (guiMessageHandler.timePulse !== previousTimePulse){
        clearInterval(guiMessageHandler.timePulseInterval)
        guiMessageHandler.timePulseInterval = setInterval(sendTimePulse, guiMessageHandler.timePulse * 1000)
        previousTimePulse = guiMessageHandler.timePulse
    }
    mqttClient.publish('time-pulse', guiMessageHandler.timePulse.toString())
    for (let ws of guis) {
	ws.send(JSON.stringify({messageType: "pulse"}))
    }
}

let previousDayNightInterval = guiMessageHandler.timeOfDayIntervalTime
function sendDayNight() {
    if (guiMessageHandler.timeOfDayIntervalTime !== previousDayNightInterval){
        clearInterval(guiMessageHandler.timeOfDayInterval)
        guiMessageHandler.timeOfDayInterval = setInterval(sendDayNight, guiMessageHandler.timeOfDayIntervalTime * 1000)
        previousDayNightInterval = guiMessageHandler.timeOfDayIntervalTime
    }
    mqttClient.publish('time-of-day', guiMessageHandler.timeOfDay.toString())
}

console.log("Server started!")
