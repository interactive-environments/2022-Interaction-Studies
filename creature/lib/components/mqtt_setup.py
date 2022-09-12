# mqtt_setup.py
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt as miniMQTT

class MQTT():

    def __init__(self, wifi, state_machines):

        try:
            from settings import settings
        except ImportError:
            print("WiFi settings are kept in settings.py, please add or change them there!")
            raise
        self.state_machines = state_machines
        self.settings = settings
        self.wifi = wifi
        self.default_topic = "time-of-day"
        miniMQTT.set_socket(socket, self.wifi.esp)
        self.mqtt_client = miniMQTT.MQTT(
            broker=settings["broker"], username=settings["user"], password=settings["token"], client_id = settings["clientid"]
        )

        self.mqtt_client.on_connect = self.connected
        self.mqtt_client.on_disconnect = self.disconnected
        self.mqtt_client.on_message = self.message

        print("Connecting to MQTT broker...")
        self.mqtt_client.connect()
        self.mqtt_client.publish("names", settings["displayname"] + "-" + settings["clientid"])

    def message(self, client, topic, message):
        if topic == "time-of-day":
            self.state_machines.setTime(int(message))
        elif topic == "energy-increment-"+settings["clientid"]:
            self.state_machines.incrementEnergy()
        print("New message on topic {0}: {1}".format(topic, message))

    ### MQTT connection functions ###
    def connected(self, client, userdata, flags, rc):
        print("Connected to MQTT broker! Listening for topic changes on %s" % self.default_topic)
        client.subscribe("time-of-day")
        client.subscribe("energy-increment-"+self.settings["clientid"])

    def disconnected(self, client, userdata, rc):
        print("Disconnected from MQTT Broker!")

    def loop(self):
        try:
            self.mqtt_client.loop()
        except (ValueError, RuntimeError) as e:
            print("Failed to get data, retrying\n", e)
            self.wifi.reset()
            self.mqtt_client.reconnect()
