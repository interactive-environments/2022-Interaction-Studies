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

print("*** Running the Great Interactive Reef Creature code...")

import components.ToF

import behaviours
import senses

from state_machines import State_machines
state_machines = State_machines(behaviours=behaviours)

from components.wifi_setup import WiFi
from components.mqtt_setup import MQTT

wifi = WiFi()
mqtt = MQTT(wifi)


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
        mqtt.loop()
    time.sleep(0.01)
