##--- Imports
import time
from timer import Timer
import board
import busio
from digitalio import DigitalInOut
import behaviour
from components import Tof
from
##--- Variables
# state_machines = State_machines(behaviours=behaviours)

# State machine variables
class State():
    idle = 0
    day_nobody = 1
    day_somebody = 2
    night_nobody = 3
    night_somebody = 4
    beautiful = 5

current_state = State.day_nobody
previous_state = State.beautiful

class Timeofday():
    day = 0
    night = 1

current_time_of_day = Timeofday.day

# Create a timer that can keep track of a person interacting
presence_timer = Timer()

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

print("*** Running the creature in isolation...")

##--- Main loop
while True:
    # Determine time of day and wheter a user is present
    senses.sense(state_machines)

    # Check which behaviour we have to run
    if current_state == State.idle:
        if step_behaviour_input.sense_release() == True:
            current_state = State.day_nobody

    elif current_state == State.day_nobody:
        run_behaviour(behaviour_rules.day_nobody_output1, behaviour_rules.day_nobody_output2, behaviour_rules.day_nobody_loops)
        if step_behaviour_input.sense_release() == True:
            current_state = State.day_somebody

    elif current_state == State.day_somebody:
        run_behaviour(behaviour_rules.day_somebody_output1, behaviour_rules.day_somebody_output2, behaviour_rules.day_somebody_loops)
        if step_behaviour_input.sense_release() == True:
            current_state = State.night_nobody

    elif current_state == State.night_nobody:
        run_behaviour(behaviour_rules.night_nobody_output1, behaviour_rules.night_nobody_output2, behaviour_rules.night_nobody_loops)
        if step_behaviour_input.sense_release() == True:
            current_state = State.night_somebody
            loops = behaviour_rules.night_somebody_loops

    elif current_state == State.night_somebody:
        run_behaviour(behaviour_rules.night_somebody_output1, behaviour_rules.night_somebody_output2, behaviour_rules.night_somebody_loops)
        if step_behaviour_input.sense_release() == True:
            current_state = State.beautiful
            loops = behaviour_rules.beautiful_loops

    elif current_state == State.beautiful:
        run_behaviour(behaviour_rules.beautiful_output1, behaviour_rules.beautiful_output2, behaviour_rules.beautiful_loops)
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

