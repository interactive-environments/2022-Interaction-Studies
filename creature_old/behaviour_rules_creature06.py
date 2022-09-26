# Varspeed declarations
MIN_OUTPUT1 = 0
MAX_OUTPUT1 = 255
MIN_OUTPUT2 = 0
MAX_OUTPUT2 = 100

# Behaviour sequences
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
day_nobody_output1 = [
   (MIN_OUTPUT1, 0, 1, "LinearInOut"),
   (160, 1.8, 80, "LinearInOut"),
   (5, 3, 80, "LinearInOut"),
]

day_nobody_output2 = [
   (MIN_OUTPUT2, 0, 1, "LinearInOut"),
   (MIN_OUTPUT2, 1.8, 80, "QuadEaseInOut"),
   (MIN_OUTPUT2, 3, 80, "QuadEaseInOut")
]
day_nobody_loops = 0

day_somebody_output1 = [
   (MAX_OUTPUT1, 0.2, 1, "LinearInOut"),
   (60, 0.3, 1, "LinearInOut"),
   (230, 0.1, 1, "LinearInOut"),
   (MIN_OUTPUT1, 0.5, 1, "LinearInOut"),
   (MAX_OUTPUT1, 0.1, 1, "LinearInOut"),
   (30, 0.2, 1, "LinearInOut")
]

day_somebody_output2 = [
   (MAX_OUTPUT2, 0.2, 1, "LinearInOut"),
   (5, 0.3, 1, "LinearInOut"),
   (90, 0.1, 1, "LinearInOut"),
   (MIN_OUTPUT2, 0.5, 1, "LinearInOut"),
   (MAX_OUTPUT2, 0.1, 1, "LinearInOut"),
   (30, 0.2, 1, "LinearInOut")
]

day_somebody_loops = 0

night_nobody_output1 = [
   (MIN_OUTPUT2, 0, 1, "LinearInOut"),
    (10, 1.8, 150, "LinearInOut"),
   (MIN_OUTPUT1, 3, 150, "LinearInOut"),
]

night_nobody_output2 = [
   (MIN_OUTPUT2, 0, 1, "LinearInOut"),
   (MIN_OUTPUT2, 1.8, 150, "LinearInOut"),
   (MIN_OUTPUT2, 3, 150, "LinearInOut")
]

night_nobody_loops = 0

night_somebody_output1 = [
   (MIN_OUTPUT1, 0, 1, "LinearInOut"),
    (10, 1.8, 10, "LinearInOut"),
   (MIN_OUTPUT1, 3, 10, "LinearInOut"),
   (100, 0.5, 10, "LinearInOut"),
   (100, 0, 1, "LinearInOut"),
   (5, 4, 10, "LinearInOut")
]

night_somebody_output2 = [
   (MIN_OUTPUT2, 0, 1, "LinearInOut"),
   (MIN_OUTPUT2, 1.8, 10, "LinearInOut"),
   (MIN_OUTPUT2, 2.5, 10, "LinearInOut"),
   (15, 0.5, 10, "LinearInOut"),
   (MIN_OUTPUT2, 0, 1, "LinearInOut"),
   (MIN_OUTPUT2, 4.5, 10, "LinearInOut")
]

night_somebody_loops = 0

beautiful_output1 = [
   (100, 1, 50, "LinearInOut"),
   (10, 0.5, 50, "LinearInOut"),
   (10, 3, 50, "LinearInOut")
]

beautiful_output2 = [
   (MIN_OUTPUT2, 1, 50, "LinearInOut"),
   (MIN_OUTPUT2, 1, 50, "LinearInOut"),
   (50, 0.2, 1, "LinearInOut"),
   (MIN_OUTPUT2, 0.2, 50, "LinearInOut"),
   (50, 0.2, 1, "LinearInOut"),
   (MIN_OUTPUT2, 1, 50, "LinearInOut"),
   (MIN_OUTPUT2, 1, 50, "LinearInOut")
]

beautiful_loops = 1
