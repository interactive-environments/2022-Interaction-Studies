# Running a creature without a connection to the spirit
# Time of day has to be set manually - try it out by changing variable current_time_of_day
# Energyy level is high when somebody is at the sensor - low when nobody is there
#
ENERGY_INCREASE_TIME = 1 # in seconds
ENERGY_DECREASE_TIME = 2 # in seconds
BEAUTIFUL_TIME = 180 # in seconds
TIME_BEING_BEAUTIFUL = 10
energy_level = 0

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
creature_input = AnalogInput()

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
# from components.button import Button
# step_behaviour_input = Button()

# --- Variables
nobody_timer = Timer()
nobody_timer.set_duration(5)
beautiful_timer = Timer()
beautiful_timer.set_duration(BEAUTIFUL_TIME)
beautiful_timer.start()
beautiful_timer2 = Timer()
beautiful_timer2.set_duration(TIME_BEING_BEAUTIFUL)

# State machine variables
class State():
    day_nobody = 1
    day_somebody = 2
    night_nobody = 3
    night_somebody = 4
    beautiful = 5

current_state = State.beautiful
previous_state = State.day_somebody

class Timeofday():
    day = 0
    night = 1

current_time_of_day = Timeofday.night

from components.wifi_setup import WiFi
from components.mqtt_setup import MQTT

wifi = WiFi()
mqtt = MQTT(wifi, current_state, current_time_of_day)

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
        position_output1 = int(position_output1 * 0.5 + position_output1 / 20 * energy_level)
#        print("position_output1 = ", position_output1)
#        output1.update_full_color((0, 0, position_output1))
#        output1.update(position_output1)
        if state == State.day_nobody or state == State.day_somebody:
            output1.update_full_color((0, 0, position_output1))
        else:
            output1.update_full_color((position_output1, 0, position_output1))

    if changed_output2 == True:
        position_output2 = int(position_output1 * 0.5 + position_output1 / 20 * energy_level)
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

def checkEnergy(company):
    global energy_level
    if nobody_timer.expired():
        if company:
            energy_level = min(10, energy_level+1)
            print(energy_level)
        else:
            energy_level = max(0, energy_level-1)
        mqtt.updateEnergy(energy_level)
        nobody_timer.start()

print("*** Running a Creature on the reef...")

# --- Main loop
while True:
    mqtt.loop()

    current_time_of_day = mqtt.timeofday
    energy_level = mqtt.energy

    # Determine the daytime and if somebody is present
    if current_time_of_day == Timeofday.day:
        if creature_input.sense(40000) == True:
            beautiful_timer.start()
            if current_state != State.day_somebody:
                nobody_timer.set_duration(ENERGY_INCREASE_TIME)
                nobody_timer.start()
                current_state = State.day_somebody
        else:
            if current_state != State.day_nobody:
                nobody_timer.set_duration(ENERGY_DECREASE_TIME)
                nobody_timer.start()
                current_state = State.day_nobody
            if beautiful_timer.expired():
                current_state = State.beautiful


    if current_time_of_day == Timeofday.night:
        if creature_input.sense(40000) == True:
            beautiful_timer.start()
            if current_state != State.night_somebody:
                nobody_timer.set_duration(ENERGY_INCREASE_TIME)
                nobody_timer.start()
                current_state = State.night_somebody
        else:
            if current_state != State.night_nobody:
                nobody_timer.set_duration(ENERGY_DECREASE_TIME)
                nobody_timer.start()
                current_state = State.night_nobody
            if beautiful_timer.expired():
                if previous_state != State.beautiful:
                    print("start")
                    beautiful_timer2.start()
                current_state = State.beautiful

    # Check which behaviour we have to run
    if current_state == State.day_nobody:
        checkEnergy(False)
        run_behaviour(behaviour_rules.day_nobody_output1, behaviour_rules.day_nobody_output2, behaviour_rules.day_nobody_loops, current_state)

    elif current_state == State.day_somebody:
        checkEnergy(True)
        run_behaviour(behaviour_rules.day_somebody_output1, behaviour_rules.day_somebody_output2, behaviour_rules.day_somebody_loops, current_state)

    elif current_state == State.night_nobody:
        checkEnergy(False)
        run_behaviour(behaviour_rules.night_nobody_output1, behaviour_rules.night_nobody_output2, behaviour_rules.night_nobody_loops, current_state)

    elif current_state == State.night_somebody:
        checkEnergy(True)
        run_behaviour(behaviour_rules.night_somebody_output1, behaviour_rules.night_somebody_output2, behaviour_rules.night_somebody_loops, current_state)

    elif current_state == State.beautiful:
        energy_level = 10
        run_behaviour(behaviour_rules.beautiful_output1, behaviour_rules.beautiful_output2, behaviour_rules.beautiful_loops, current_state)
        if beautiful_timer2.expired():
            energy_level = 0
            beautiful_timer.start()

    # Print the current state if it has changed
    if previous_state != current_state:
        previous_state = current_state
        if current_state == State.day_nobody:
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
