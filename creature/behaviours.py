# import time
# import board
# import p9813

# To use the LED, change num_leds to the amount of LEDS that are attached to each other.
# The update function takes an RGB color.
from components.led import LED
num_leds = 1
leds = LED(num_leds)
# leds.update((0, 255, 0))

# The update function for the buzzer takes a value between 0 and 100.
from components.buzzer import Buzzer
buzzer = Buzzer()
# buzzer.update(3)

# The update function for the vibration motor takes either True or False.
from components.vibration_motor import Vibration_Motor
vibration_motor = Vibration_Motor()
# vibration_motor.update(True)

# The update function for the servo motor takes a value between 0 and 180.
from components.servo_motor import Servo
servo = Servo()
# servo.update(100)

# this is the current energy level of the creature
energy = 0

# BEHAVIOUR FOR OUTPUT 1
# first set the the output for this behaviour
output_1 = leds
# Theses are the min and maximum value of the outputs
output_1_INTITIAL = 0
output_1_MAX = 255
output_1_MIN = 0

# this is the behaviour sequence for when someone is interacting by during the day
output_1_day_no_company_behaviour = [(output_1_MAX, 15/(energy+1), 200, "QuadEaseIn"),(output_1_MIN, 15/(energy+1), 200, "QuadEaseOut")]
# this is the behaviour sequence for when someone is not by during the day
output_1_day_company_behaviour = [(output_1_MAX, 5/(energy+1), 200, "QuadEaseIn"),(output_1_MIN, 5/(energy+1), 200, "QuadEaseOut")]
# this is the behaviour sequence for when someone is interacting by during the night
output_1_night_no_company_behaviour = [(output_1_MAX/2, 15/(energy+1), 200, "QuadEaseIn"),(output_1_MIN, 15/(energy+1), 200, "QuadEaseOut")]
# this is the behaviour sequence for when someone is not by during the night
output_1_night_company_behaviour = [(output_1_MAX/2, 5/(energy+1), 200, "QuadEaseIn"),(output_1_MIN, 5/(energy+1), 200, "QuadEaseOut")]

# BEHAVIOUR FOR OUTPUT 2
# first set the the output for this behaviour
output_2 = buzzer
# Theses are the min and maximum value of the outputs
output_2_INTITIAL = 0
output_2_MAX = 100
output_2_MIN = 0

# this is the behaviour sequence for when someone is interacting by during the day
output_2_day_no_company_behaviour = [(output_2_MAX, 15/(energy+1), 200, "QuadEaseIn"),(output_2_MIN, 15/(energy+1), 200, "QuadEaseOut")]
# this is the behaviour sequence for when someone is not by during the day
output_2_day_company_behaviour = [(output_2_MAX/2, 5/(energy+1), 200, "QuadEaseIn"),(output_2_MIN/2, 5/(energy+1), 200, "QuadEaseOut")]
# this is the behaviour sequence for when someone is interacting by during the night
output_2_night_no_company_behaviour = [(output_2_MAX, 15/(energy+1), 200, "QuadEaseIn"),(output_2_MIN, 15/(energy+1), 200, "QuadEaseOut")]
# this is the behaviour sequence for when someone is not by during the night
output_2_night_company_behaviour = [(output_2_MAX/2, 5/(energy+1), 200, "QuadEaseIn"),(output_2_MIN/2, 5/(energy+1), 200, "QuadEaseOut")]


# CODE FOR EXECUTING BEHAVIOURS

def behave_day_no_company(output_1_behaviour_value, output_2_behaviour_value):
    output_1.update((0, output_1_behaviour_value, 0))
    output_2.update(output_2_behaviour_value)

def behave_day_company(output_1_behaviour_value, output_2_behaviour_value):
    output_1.update((0, output_1_behaviour_value, 0))
    output_2.update(output_2_behaviour_value)

def behave_night_no_company(output_1_behaviour_value, output_2_behaviour_value):
    output_1.update((0, output_1_behaviour_value, 0))
    output_2.update(output_2_behaviour_value)

def behave_night_company(output_1_behaviour_value, output_2_behaviour_value):
    output_1.update((0, output_1_behaviour_value, 0))
    output_2.update(output_2_behaviour_value)



# old code, dit wordt denk ik vanaf nu door Caspar's code geregeld:
# pin_clk = board.D13
# pin_data = board.D10
# num_leds = 1
# leds = p9813.P9813(pin_clk, pin_data, num_leds)

# leds.fill((0, 0, 0))
# leds.write()

# def showAlive():
#     leds.fill((255, 255, 255))
#     leds.write()
#     time.sleep(0.5)
#     leds.fill((0, 0, 0))
#     leds.write()
#     time.sleep(0.5)
#     leds.fill((255, 255, 255))
#     leds.write()
#     time.sleep(0.5)
#     leds.fill((0, 0, 0))
#     leds.write()
#     time.sleep(0.5)
#     return

# def behaveDayNoCompany(energy):
#     leds.fill((10+(energy*5), 10+(energy*5), 0))
#     leds.write()
#     return

# def behaveDayCompany(energy):
#     leds.fill((100+(energy*15), 100+(energy*15), 0))
#     leds.write()
#     return

# def behaveNightNoCompany(energy):
#     leds.fill((0, 0, 10+(energy*5)))
#     leds.write()
#     return

# def behaveNightCompany(energy):
#     leds.fill((0, 0, 100+(energy*15)))
#     leds.write()
#     return

# def behaveInvitinglyBeautiful(energy):
#     leds.fill((255, 255, 255))
#     leds.write()
#     return

