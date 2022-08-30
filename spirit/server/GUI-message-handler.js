const CREATURE_COUNT = 15
const NEIGHBOUR_ENERGY_DIFFERENCE = 2
const TIME_OUT_IN_MINUTES = 10

export class GUIMessageHandler {
    constructor(mqtt) {
        this.timeOfDay = 0;
        this.timeOfDayIntervalTime = 5;
        this.timeOfDayInterval = null;


        this.timePulse = 10.5;
        this.timePulseInterval = null;

        this.creatures = [];

        for (let i = 0; i < CREATURE_COUNT; i++) {
            this.creatures.push(new Creature(i, mqtt))
        }

        this.mqtt = mqtt;

    }

    getName(data, guis) {
        let id = data.split("-")
        id = id[id.length-1]

        const creature = this.creatures[id]

        // Index doesn't exists
        if (!creature)
            return

        // set the name
        let name = data.split("-")
        name = name.splice(0, name.length-1).join("-")
        creature.name = name

        // send data
        sendAddedToGUIs(creature, guis)

        // set timeout
        clearTimeout(creature.timeout)
        creature.timeout = setTimeout(() => {sendTimeOutToGUIs(creature, guis)}, TIME_OUT_IN_MINUTES * 1000 * 60)
    }

    changeCreatureEnergy(creatureId, energy, guis) {
        const creature = this.creatures[creatureId]

        // Index doesn't exists
        if (!creature)
            return

        // update timeout
        clearTimeout(creature.timeout)
        creature.timeout = setTimeout(() => {sendTimeOutToGUIs(creature, guis)}, TIME_OUT_IN_MINUTES * 1000 * 60)

        // update that creature
        creature.updateEnergy(energy, guis)
    }

    changeDayNight(dataObject) {
        if (typeof dataObject.timeOfDay === "undefined")
            return

        if (dataObject.timeOfDay === 0 || dataObject.timeOfDay === 1)
            this.timeOfDay = dataObject.timeOfDay
    }

    changeTimePulse(dataObject) {
        if (typeof dataObject.newInterval === "undefined")
            return

        const typeCheck = Number(dataObject.newInterval)
        if (!isNaN(typeCheck))
            this.timePulse = dataObject.newInterval
    }

    setNeighbours(dataObject) {
        const neighbours = dataObject.neighbours
        for (const [key, neighbourList] of Object.entries(neighbours)) {
            const creature = this.creatures[key]
            if (!creature)
                continue
            // clear old list
            creature.neighbours = []
            // add neighbours
            for (const neighbour of neighbourList) {
                const n = this.creatures[neighbour]
                if (!n)
                    continue
                creature.addNeighbour(n)
            }
        }
    }

    sendNeighbours(guis) {
        const neighbourList = {}
        for (let i = 0; i < this.creatures; i++) {
            const creature = this.creatures[i]
            // Check if we should include this creature
            if (!creature || !creature.neighbours || creature.neighbours.length === 0)
                continue

            // Add the neighbours
            const list = []
            for (const neighbour of creature.neighbours) {
                list.push(neighbour.clientId)
            }
            // save list
            neighbourList[i] = list
        }

        sendNeighboursGUIs(neighbourList, guis)
    }
}

class Creature {
    constructor(clientId,mqtt) {
        this.clientId = clientId
        this.name = ""
        this.mqtt = mqtt;

        this.energyLevel = 1;
        this.neighbours = [];

        this.timeout = null
    }

    updateEnergy(energy, guis) {
        this.energyLevel = energy;
        sendEnergyUpdateToGUIs(this, guis)
        sendEnergyUpdateToMqtt(this, this.mqtt)
    }

    addNeighbour(creature) {
        this.neighbours.push(creature)
    }
}

function sendEnergyUpdateToGUIs(creature, guis) {
    for (let ws of guis) {
        ws.send(JSON.stringify({
            messageType: "updateEnergy",
            name: creature.name,
            energy: creature.energyLevel
        }))
    }
}

function sendEnergyUpdateToMqtt(creature, mqtt) {
    // Go through all neighbors
    if (!creature.neighbours || creature.neighbours.length === 0)
        return

    for (let neighbour of creature.neighbours) {
        if (!neighbour)
            return

        if (neighbour.energyLevel <= creature.energyLevel - NEIGHBOUR_ENERGY_DIFFERENCE) {
            mqtt.publish(`energy-increment-${neighbour.clientId}`, "1")
        }
    }
}

function sendAddedToGUIs(creature, guis) {
    for (let ws of guis) {
        ws.send(JSON.stringify({
            messageType: "addCreature",
            name: creature.name,
            energy: creature.energyLevel
        }))
    }
}

function sendTimeOutToGUIs(creature, guis) {
    console.log("Creature timed out")
    for (let ws of guis) {
        ws.send(JSON.stringify({
            messageType: "timeoutCreature",
            name: creature.name,
            energy: creature.energyLevel
        }))
    }
}

function sendNeighboursGUIs(list, guis) {
    console.log("send list")
    for (let ws of guis) {
        ws.send(JSON.stringify({
            messageType: "neighbours",
            neighbours: list
        }))
    }
}