# Creature behaviour designing made simple
# This file runs a statemachine with all required behaviours as states
# Simply connect a button to A0, each button press will step to the next behaviour
# Watch the serial monitor to determine which behaviour is active (the active state will be printed)

# To design the behaviour including the energy parameter

# --- Libraries
import time
import board
import components.button
from varspeed import Vspeed
from timer import Timer

# Creature input
from components.analog_input import AnalogInput
from components.tof import Tof

# Possible output components
from components.led import LED
from components.servo_motor import Servo
from components.buzzer import Buzzer
from components.vibration_motor import VibrationMotor
from components.electro_magnet import ElectroMagnet

# Simulating a person input with the energy slider/rotation sensor
energy_input = AnalogInput()
# energy_input = Tof()

# Import the bahaviour rules
# import behaviour_rules
import behaviour_rules_creature06 as behaviour_rules

# Define the ouputs of creature01
# output1 = LED(2)
# output2 = Buzzer()

# Define the outputs of creature02
# output1 = Buzzer()
# output2 = Servo()
# output3 = LED(1)

# Define the outputs of creature03
# output1 = VibrationMotor()
# output2 = Servo()

# Define the outputs of creature04
# output1 = Servo()
# output2 = VibrationMotor()

# Define the outputs of creature05
# output1 = LED(1)
# output2 = ElectroMagnet()

# Define the outputs of creature06
output1 = LED(1)
output2 = Buzzer()

# Define the outputs of creature07

# Define the outputs of creature08
# output1 = VibrationMotor()
# output2 = Servo()

# Define the outputs of creature09
# output1 = LED(1)
# output2 = Buzzer()

# Define the outputs of creature10

# -------------------------
# do not change anything below this line

# Using the Button to step through all the behaviours
from components.button import Button
step_behaviour_input = Button()

# --- Variables
timer = Timer()
timer.set_duration(3)

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

# init_position = initial start position // result = float, int
vs_output1 = Vspeed(init_position=0, result="int")
vs_output2 = Vspeed(init_position=0, result="int")

# make the output of the function be within the bounds set
# vs_output1.set_bounds(lower_bound=MIN_OUTPUT1, upper_bound=MAX_OUTPUT1)
# vs_output2.set_bounds(lower_bound=MIN_OUTPUT2, upper_bound=MAX_OUTPUT2)

def run_behaviour(output1_sequence, output2_sequence, loops, state):
    position_output1, running_output1, changed_output1 = vs_output1.sequence(sequence=output1_sequence, loop_max=loops)
    position_output2, running_output2, changed_output2 = vs_output2.sequence(sequence=output2_sequence, loop_max=loops)
    if changed_output1 == True:
        position_output1 = int(position_output1 / 10 * energy_level)
#        print("position_output1 = ", position_output1)
#        output1.update_full_color((0, 0, position_output1))
#        output1.update(position_output1)
        if state == State.day_nobody or state == State.day_somebody:
            output1.update_full_color((0, 0, position_output1))
        else:
            output1.update_full_color((position_output1, 0, position_output1))
    if changed_output2 == True:
        position_output2 = int(position_output2 / 10 * energy_level)
#        print("position_output2 = ", position_output2)
        output2.update(position_output2)

# To map a number from one range to another, we just need to apply some math to the number.
def map_to_range(x, fromMin, fromMax, toMin, toMax):
   # Get the total "amount" of numbers between our minimum and maximum. For example if we want to go between 1 and 3, this will be 2.d
   fromTotal = fromMax - fromMin

   # Same as previous but for the minimum and maximum we want to work towards.
   toTotal = toMax - toMin

   # Divide the To by the From to see how much bigger (or smaller) the To is compared to the From.
   multiplier = toTotal / fromTotal

   # If our number is at the minimum, we want it to be at 0. This makes multiplying easier.
   y = x - fromMin

   # Multiply said number by our multiplier so we get the correct range. For example a range from 0,1 turns into 0,180 by multiplying by 180.
   z = y * multiplier

   # We get the result by adding the minimum of the To to our previous result.
   result = z + toMin
   return result # Return

print("*** Running the Creature Designer code...")

# --- Main loop
while True:
    # Obtain the current energy level from the analog input on A4
    energy_level = int(map_to_range(energy_input.sense_value(), 0, 65536, 1, 10))
#    energy_level = int(map_to_range(energy_input.sense_range(), 8200, 50, 1, 10))

    # Check which behaviour we have to run
    if current_state == State.idle:
        if step_behaviour_input.sense_release() == True:
            current_state = State.day_nobody

    elif current_state == State.day_nobody:
        run_behaviour(behaviour_rules.day_nobody_output1, behaviour_rules.day_nobody_output2, behaviour_rules.day_nobody_loops, current_state)
        if step_behaviour_input.sense_release() == True:
            current_state = State.day_somebody

    elif current_state == State.day_somebody:
        run_behaviour(behaviour_rules.day_somebody_output1, behaviour_rules.day_somebody_output2, behaviour_rules.day_somebody_loops, current_state)
        if step_behaviour_input.sense_release() == True:
            current_state = State.night_nobody

    elif current_state == State.night_nobody:
        run_behaviour(behaviour_rules.night_nobody_output1, behaviour_rules.night_nobody_output2, behaviour_rules.night_nobody_loops, current_state)
        if step_behaviour_input.sense_release() == True:
            current_state = State.night_somebody
            loops = behaviour_rules.night_somebody_loops

    elif current_state == State.night_somebody:
        run_behaviour(behaviour_rules.night_somebody_output1, behaviour_rules.night_somebody_output2, behaviour_rules.night_somebody_loops, current_state)
        if step_behaviour_input.sense_release() == True:
            current_state = State.beautiful
            loops = behaviour_rules.beautiful_loops

    elif current_state == State.beautiful:
        energy_level = 10
        run_behaviour(behaviour_rules.beautiful_output1, behaviour_rules.beautiful_output2, behaviour_rules.beautiful_loops, current_state)
        if step_behaviour_input.sense_release() == True:
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
