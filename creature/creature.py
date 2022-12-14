# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
from timer import Timer
timer = Timer()
timer.set_duration(3)
import board
import busio
from digitalio import DigitalInOut
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt as MQTT

print("Running the Great interactive reef code.")

### WiFi ###
# Get wifi details and more from a secrets.py file
# try:
#     from settings import settings
# except ImportError:
#     print("WiFi settings are kept in settings.py, please add or change them there!")
#     raise

import components.ToF

import behaviours
import senses

from state_machines import State_machines
state_machines = State_machines(behaviours=behaviours)


# If you have an externally connected ESP32:
# esp32_cs = DigitalInOut(board.D9)               # Chip select pin
# esp32_ready = DigitalInOut(board.D11)           # BUSY or READY pin
# esp32_reset = DigitalInOut(board.D12)           # Reset pin

# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

# wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, settings)

# Setup a feed named `testfeed` for publishing.
# default_topic = "time-of-day"

### Code ###

### Helper functions ###
# def message(client, topic, message):
#     if topic == "time-of-day":
#         state_machines.setTime(int(message))
#     elif topic == "energy-increment-"+settings["clientid"]:
#         state_machines.incrementEnergy()
#     print("New message on topic {0}: {1}".format(topic, message))

### MQTT connection functions ###
# def connected(client, userdata, flags, rc):
#     print("Connected to MQTT broker! Listening for topic changes on %s" % default_topic)
#     client.subscribe("time-of-day")
#     client.subscribe("energy-increment-"+settings["clientid"])

# def disconnected(client, userdata, rc):
#     print("Disconnected from MQTT Broker!")

# Connect to WiFi
# print("Connecting to WiFi...")
# wifi.connect()
# print("Connected!")

# MQTT.set_socket(socket, esp)
# mqtt_client = MQTT.MQTT(
#     broker=settings["broker"], username=settings["user"], password=settings["token"], client_id = settings["clientid"]
# )

# mqtt_client.on_connect = connected
# mqtt_client.on_disconnect = disconnected
# mqtt_client.on_message = message

# print("Connecting to MQTT broker...")
# mqtt_client.connect()
# mqtt_client.publish("names", settings["displayname"] + "-" + settings["clientid"])

while True:
    senses.sense(state_machines)
#     state_machines.behave(behaviours, mqtt_client)
    state_machines.behave(behaviours)

#     print(last_state, state_machines.state)
    if (state_machines.last_state == 0 or state_machines.last_state == 2) and (state_machines.state == 1 or state_machines.state == 3):
        print("Presence detected")
    elif (state_machines.last_state == 1 or state_machines.last_state == 3) and (state_machines.state == 0 or state_machines.state == 2):
        print("Presence no longer detected")

    if (state_machines.last_state == 0 or state_machines.last_state == 1) and (state_machines.state == 2 or state_machines.state == 3):
        print("It is now daytime.")
    if (state_machines.last_state == 2 or state_machines.last_state == 3) and (state_machines.state == 0 or state_machines.state == 1):
        print("It is now nighttime.")

    if timer.expired:
        timer.start()
#         try:
#             mqtt_client.loop()
#         except (ValueError, RuntimeError) as e:
#             print("Failed to get data, retrying\n", e)
#             wifi.reset()
#             mqtt_client.reconnect()
#             continue
    time.sleep(0.01)
