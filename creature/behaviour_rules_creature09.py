# Varspeed declarations
MIN_OUTPUT1 = 0
MAX_OUTPUT1 = 255
MIN_OUTPUT2 = 0
MAX_OUTPUT2 = 100

# Behaviour sequences
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
day_nobody_output1 = [
   (MAX_OUTPUT1, 2, 5, "LinearInOut"),
   (MIN_OUTPUT1, 2, 5, "LinearInOut"),
]

day_nobody_output2 = [
   (MAX_OUTPUT2, 5, 5, "QuadEaseInOut"),
   (MIN_OUTPUT2, 5, 5, "QuadEaseInOut")
]
day_nobody_loops =1

day_somebody_output1 = [
   (0, 1.0, 1, "LinearInOut"),
   (MAX_OUTPUT1, 5, 8, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (0, 10.0, 11, "LinearInOut")
]

day_somebody_output2 = [
   (10, 0.01, 1, "LinearInOut"),
   (MIN_OUTPUT2, 0.01, 1, "LinearInOut")
]

day_somebody_loops = 1

night_nobody_output1 = [
   (0, 1.0, 1, "LinearInOut"),
   (MAX_OUTPUT1, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (0, 10.0, 11, "LinearInOut")
]

night_nobody_output2 = [
   (MAX_OUTPUT2, 5, 5, "QuadEaseInOut"),
   (MIN_OUTPUT2, 5, 5, "QuadEaseInOut")
]

night_nobody_loops = 2

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

night_somebody_loops =1

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

beautiful_loops = 1
