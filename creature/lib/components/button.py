# button.py

import board
import digitalio

class Button():
    previous_button_value = False
    
    def __init__(self):
        self.button = digitalio.DigitalInOut(board.D2)
        self.button.direction = digitalio.Direction.INPUT


    def sense(self):
        current_button_value = self.button.value
        button_status = False
        
        # Only trigger on button release
        if (self.previous_button_value == True and current_button_value == False):
            button_status = True

        self.previous_button_value = current_button_value
        
        return button_status
