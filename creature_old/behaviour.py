##--- Imports
from varspeed import Vspeed
from components.led import LED
from components.buzzer import Buzzer
from components.servo_motor import Servo
from components.vibration_motor import VibrationMotor

##--- Variables
num_leds = 1
leds = LED(num_leds)
buzzer = Buzzer()
vibration_motor = VibrationMotor()
servo = Servo()

# this is the current energy level of the creature
energy = 1

# Import the bahaviour rules
import behaviour_rules

# Define the ouputs of your creature
output1 = LED(1)
output2 = Servo()
#output2 = Buzzer()
#output2 = ElectroMagnet()
#output2 = VibrationMotor()

# init_position = initial start position // result = float, int
vs_output1 = Vspeed(init_position=0, result="int")
vs_output2 = Vspeed(init_position=0, result="int")

##--- Functions
def run_behaviour(output1_sequence, output2_sequence, loops):
    position_output1, running_output1, changed_output1 = vs_output1.sequence(sequence=output1_sequence, loop_max=loops)
    position_output2, running_output2, changed_output2 = vs_output2.sequence(sequence=output2_sequence, loop_max=loops)
    if changed_output1 == True:
        position_output1 = int(position_output1 / 10 * energy_level)
        print("position_output1 = ", position_output1)
        output1.update_full_color((0, position_output1, 0))
    if changed_output2 == True:
        position_output2 = int(position_output2 / 10 * energy_level)
        print("position_output2 = ", position_output2)
        output2.update(position_output2)

def behave_day_no_company(output_1_behaviour_value, output_2_behaviour_value):
    output_1.update_full_color((0, output_1_behaviour_value, 0))
    output_2.update(output_2_behaviour_value)


def behave_day_company(output_1_behaviour_value, output_2_behaviour_value):
    output_1.update_full_color((0, output_1_behaviour_value, 0))
    output_2.update(output_2_behaviour_value)


def behave_night_no_company(output_1_behaviour_value, output_2_behaviour_value):
    output_1.update_full_color((0, output_1_behaviour_value, 0))
    output_2.update(output_2_behaviour_value)


def behave_night_company(output_1_behaviour_value, output_2_behaviour_value):
    output_1.update_full_color((0, 0, output_1_behaviour_value))
    output_2.update(output_2_behaviour_value)
