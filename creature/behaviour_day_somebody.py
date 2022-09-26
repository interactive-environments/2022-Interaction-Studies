

# The maximum value of output 1
OUTPUT_1_MAX = 255
# The minimum value of output 1
OUTPUT_1_MIN = 0
# The amount of loops for output 1
# zero means infinite
OUTPUT_1_LOOPS = 0

OUTPUT_1_SEQUENCE = [
   (OUTPUT_1_MAX, 5, 10, "LinearInOut"),
   (OUTPUT_1_MIN, 5, 10, "LinearInOut"),
]

# The maximum value of output 2
OUTPUT_2_MAX = 255
# The minimum value of output 2
OUTPUT_2_MIN = 0
# The amount of loops for output 2
# zero means infinite
OUTPUT_2_LOOPS = 0

OUTPUT_2_SEQUENCE = [
   (OUTPUT_2_MAX, 5, 10, "LinearInOut"),
   (OUTPUT_2_MIN, 5, 10, "LinearInOut"),
]

def update_outputs(sequence_1_value, sequence_2_value, energy):
    global output_1
    global output_2

    value_1 = min(OUTPUT_1_MAX, sequence_1_value * energy)
    value_2 = min(OUTPUT_2_MAX, sequence_2_value * energy)

    output_1.update(value_1)
    output_2.update(value_2)
