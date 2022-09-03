import board
from analogio import AnalogIn

# For use with a button or touch sensor:

# from components.button import Button
# button = Button()

# def sense(state_machines):
#     if button.sense():
#         state_machines.setCompany(1)
#         state_machines.incrementEnergy()
#     else:
#         state_machines.setCompany(0)


# For use with a time-of-flight sensor. ToF sense compares the measured distance to the provided distance in mm:

from components.ToF import ToF
ToF = ToF()

def sense(state_machines):
    if ToF.sense(100):
        state_machines.setCompany(1)
    else:
        state_machines.setCompany(0)
