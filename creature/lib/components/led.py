# led.py

import board
import p9813

class LED():
    def __init__(self, num_leds):
        self.pin_clk = board.D13
        self.pin_data = board.D10
        self.num_leds = num_leds
        self.leds = p9813.P9813(self.pin_clk, self.pin_data, self.num_leds)

    def update(self, color):
        self.leds.fill(color)
        self.leds.write()
