# ToF.py

import time
import board
import busio
import adafruit_vl53l0x

import board
from analogio import AnalogIn

class ToF():
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.vl53 = adafruit_vl53l0x.VL53L0X(self.i2c)

    def sense(self, distance):
        return self.vl53.range < distance
