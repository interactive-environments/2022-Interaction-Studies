# Creature behaviour testing made simple
# This file runs a statemachine with all required behaviours as states
# Simply connect a button to D2, each button press will step to the next behaviour
# Watch the serial monitor to determine which behaviour is active
# If you want the full experience then be sure to attach a Chainable LED to D13, an Analog Servo to D4 and a Sliding Potentiometer (slider) to A0
#

# --- Libraries
import time
import board
import components.button
#import behaviours
from varspeed import Vspeed
from timer import Timer
from components.button import Button
from components.led import LED
from components.servo_motor import Servo
from analogio import AnalogIn

analog_in = AnalogIn(board.A0)
# --- Variables
timer = Timer()
timer.set_duration(3)

# Working with a button to trigger behaviour changes
button = Button()

# State machine variables
class State():
    idle = 0
    day_nobody = 1
    day_somebody = 2
    night_nobody = 3
    night_somebody = 4
    beautiful = 5

current_state = State.idle
previous_state = State.beautiful

# Varspeed declarations
MIN_OUTPUT1 = 0
MAX_OUTPUT1 = 255
MIN_OUTPUT2 = 0
MAX_OUTPUT2 = 180

# init_position = initial start position // result = float, int
vs_output1 = Vspeed(init_position=MIN_OUTPUT1, result="int")
vs_output2 = Vspeed(init_position=MIN_OUTPUT2, result="int")

# make the output of the function be within the bounds set
vs_output1.set_bounds(lower_bound=MIN_OUTPUT1, upper_bound=MAX_OUTPUT1)
vs_output2.set_bounds(lower_bound=MIN_OUTPUT2, upper_bound=MAX_OUTPUT2)

# Behaviour sequences
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
day_nobody_output1 = [
   (MAX_OUTPUT1, 5, 10, "LinearInOut"),
   (MIN_OUTPUT1, 5, 10, "LinearInOut"),
]

day_nobody_output2 = [
   (MAX_OUTPUT2, 5, 5, "QuadEaseInOut"),
   (MIN_OUTPUT2, 5, 5, "QuadEaseInOut")
]

day_somebody_output1 = [
   (0, 1.0, 1, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (0, 10.0, 11, "LinearInOut")
]

day_somebody_output2 = [
   (10, 0.01, 1, "LinearInOut"),
   (MIN_OUTPUT2, 0.01, 1, "LinearInOut")
]

night_nobody_output1 = [
   (0, 1.0, 1, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (0, 10.0, 11, "LinearInOut")
]

night_nobody_output2 = [
   (10, 0.01, 1, "LinearInOut"),
   (MIN_OUTPUT2, 0.01, 1, "LinearInOut")
]

night_somebody_output1 = [
   (0, 1.0, 1, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (0, 10.0, 11, "LinearInOut")
]

night_somebody_output2 = [
   (10, 0.01, 1, "LinearInOut"),
   (MIN_OUTPUT2, 0.01, 1, "LinearInOut")
]

beautiful_output1 = [
   (0, 1.0, 1, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (0, 10.0, 11, "LinearInOut")
]

beautiful_output2 = [
   (10, 0.01, 1, "LinearInOut"),
   (MIN_OUTPUT2, 0.01, 1, "LinearInOut")
]

output1 = LED(1)
output2 = Servo()

def run_behaviour(output1_sequence, output2_sequence, energy):
    position_output1, running_output1, changed_output1 = vs_output1.sequence(sequence=output1_sequence, loop_max=1)
    position_output2, running_output2, changed_output2 = vs_output2.sequence(sequence=output2_sequence, loop_max=1)
    if changed_output1 == True:
        print("position_output1 = ", (position_output1 * (10+energy)/20))
        output1.update((0, int(position_output1 * (10+energy)/20), 0))
    if changed_output2 == True:
        output2.update(int(position_output2 * (10+energy)/20))
        print("position_output2 = ", (position_output2 * (10+energy)/20))

# --- Main loop
while True:
    energy = int(analog_in.value*11/65536)
    if current_state == State.idle:
        if button.sense() == True:
            current_state = State.day_nobody

    elif current_state == State.day_nobody:
        run_behaviour(day_nobody_output1, day_nobody_output2, energy)
        if button.sense() == True:
            current_state = State.day_somebody

    elif current_state == State.day_somebody:
        run_behaviour(day_somebody_output1, day_somebody_output2, energy)
        if button.sense() == True:
            current_state = State.night_nobody

    elif current_state == State.night_nobody:
        run_behaviour(night_nobody_output1, night_nobody_output2, energy)
        if button.sense() == True:
            current_state = State.night_somebody

    elif current_state == State.night_somebody:
        run_behaviour(night_somebody_output1, night_somebody_output2, energy)
        if button.sense() == True:
            current_state = State.beautiful

    elif current_state == State.beautiful:
        run_behaviour(beautiful_output1, beautiful_output2, energy)
        if button.sense() == True:
            current_state = State.idle

    # Print the current state if it has changed
    if previous_state != current_state:
        previous_state = current_state
        if current_state == State.idle:
            print("*** idle state")
        elif current_state == State.day_nobody:
            print("*** day_nobody behaviour")
        elif current_state == State.day_somebody:
            print("*** day_somebody behaviour")
        elif current_state == State.night_nobody:
            print("*** night_nobody behaviour")
        elif current_state == State.night_somebody:
            print("*** night_somebody behaviour")
        elif current_state == State.beautiful:
            print("*** beautiful behaviour")
    
    time.sleep(0.01)



