# Spirit Management-server

This server connects to the Mqtt server and the controller webpage. To connect to the webpage it uses websockets that by default use port `3001`.

## Connecting to mqtt
The spirit connects to the mqtt broker in order to communicate all the relevant information to the creatures.
In order to change this connection the `server.js` file can be edited.

To change the url see `line 6` til `line 10` of `server.js`
```js
const mqttClient  = mqtt.connect('mqtts://greatinteractivereef.cloud.shiftr.io/', {
    clientId: "Spirit",
    username: "greatinteractivereef",
    password: "<PASSWORD>"
})
```
`clientId` is the id of the server in the mqtt broker and should be "spirit".
`username` and `pasword` are the connection details of the mqtt broker. For shifter.io the password will be the token of the instance.

## Constants
at the top of the file `GUI-message-handler.js` are a selection of constants. These constants change the working of the spirit.
- `CREATURE_COUNT` is the amount of creatures that there can be in the reef.
- `NEIGHBOUR_ENERGY_DIFFERENCE` is the difference in energy level that has to be preserved during neighbour propagation.
For example if "node-1" has an energy of 10 then its neighbour "node-2" can get at most a value of 8 from "node-1"
- `TIME_OUT_IN_MINUTES` is the time in minutes it takes before the UI marks a creature as offline.