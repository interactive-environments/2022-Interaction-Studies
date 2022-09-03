# button.py

import board
from analogio import AnalogIn

class Button():
    def __init__(self):
        self.button = AnalogIn(board.A0)

    def sense(self):
        return self.button.value > 60000
