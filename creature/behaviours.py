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

