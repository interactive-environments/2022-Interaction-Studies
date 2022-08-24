import board
import digitalio

button = digitalio.DigitalInOut(board.D7)

def sense(state_machines):
    if button.value:
        state_machines.setCompany(1)
    else:
        state_machines.setCompany(0)
