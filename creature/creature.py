# This is the creature file.
# This file specifies the physic of the creature.
# In here you will specify what inputs and outputs the creature has.

# TODO Ecosystem or Behaviour Creator mode
# TODO This loads the mqtt or adds a button for the state changes

# -------------------------------
# ---------  THE LIMBS ----------
# -------------------------------

# ----------- THE INPUT ---------
# here we register what input the creature uses
# uncomment one of the import lines to use that input component
from components.button import Button
# from components.analog_input import AnalogInput
# from components.slider import Slider
# from components.tof import Tof

input = Button()

# -------------------------------

# ----------- OUTPUT 1 ---------
# here we register the first output for the creature
# uncomment one of the import lines to use that output component
from componetns.Buzzer import Buzzer

output_1 = Buzzer()

# -------------------------------


# ----------- OUTPUT 2 ---------
# here we register what input the creature uses
# uncomment one of the import lines to use that output component
from components.Buzzer import Buzzer

output_2 = Buzzer()

# -------------------------------


# -------------------------------
# ---------  THE BRAIN ----------
# -------------------------------
# Below here we load all the helper functions needed to execute all behaviour and keep track of the states.
# You should not need to change anything below here.
# In order to change the behaviour take a look at the behaviour files.
from behaviour import Behaviour
from state_machines import StateMachine

state_machine = StateMachine()

# ----------- BEHAVIOUR ---------
# Here we load all types of behaviour the creature could display

# TODO make a Idle behaviour that sets all outputs to off
# -- Behaviour 1: Idle
state_machine.states[0] = Behaviour("Idle")
# -----

# -- Behaviour 2: Day time - Nobody
import behaviour_day_nobody as behaviour_2
state_machine.states[1] = Behaviour(
    "Day_Nobody",
    behaviour_2.OUTPUT_1_SEQUENCE,
    behaviour_2.OUTPUT_2_SEQUENCE,
    behaviour_2.update_outputs)
# ----

# -- Behaviour 3: Day time - Somebody
import behaviour_day_somebody as behaviour_3
state_machine.states[2] = Behaviour(
    "Day_Somebody",
    behaviour_3.OUTPUT_1_SEQUENCE,
    behaviour_3.OUTPUT_2_SEQUENCE,
    behaviour_3.update_outputs)
# ----

# -- Behaviour 4: Night time - Nobody
import behaviour_night_nobody as behaviour_4
state_machine.states[3] = Behaviour(
    "Night_Nobody",
    behaviour_4.OUTPUT_1_SEQUENCE,
    behaviour_4.OUTPUT_2_SEQUENCE,
    behaviour_4.update_outputs)
# ----

# -- Behaviour 5: Night time - Somebody
import behaviour_night_somebody as behaviour_5
state_machine.states[4] = Behaviour(
    "Night_Somebody",
    behaviour_5.OUTPUT_1_SEQUENCE,
    behaviour_5.OUTPUT_2_SEQUENCE,
    behaviour_5.update_outputs)
# ----

# -- Behaviour 6: Beautiful
import behaviour_beautiful as behaviour_6
state_machine.states[5] = Behaviour(
    "Beautiful",
    behaviour_6.OUTPUT_1_SEQUENCE,
    behaviour_6.OUTPUT_2_SEQUENCE,
    behaviour_6.update_outputs)
# ----

# -------------------------------

# -------- STATE CHANGES --------

# TODO state transition rules

# -------------------------------

