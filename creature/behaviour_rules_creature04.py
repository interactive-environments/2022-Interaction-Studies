# Varspeed declarations
MIN_OUTPUT1 = 0
MAX_OUTPUT1 = 180
MIN_OUTPUT2 = 0
MAX_OUTPUT2 = 100

# Behaviour sequences
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
day_nobody_output1 = [
   (0, 1, 1, "LinearInOut"),
   (120, 3, 15, "LinearInOut"),
   (0, 3, 15, "LinearInOut"),
   (120, 3, 15, "LinearInOut"),

]

day_nobody_loops = 0

day_nobody_output2 = [
   (100, 2, 5, "QuadEaseInOut"),
   (0, 2, 5, "QuadEaseInOut"),
   (100, 2, 5, "QuadEaseInOut"),
   (0, 2, 5, "QuadEaseInOut")
]

day_somebody_output1 = [
   (120, 0.5, 1, "LinearInOut"),
   (0, 2, 1, "LinearInOut"),

]

day_somebody_output2 = [
   (MAX_OUTPUT2 , 0.5, 5, "QuadEaseInOut"),
   (MIN_OUTPUT2 , 0.5, 5, "QuadEaseInOut"),
   (MAX_OUTPUT2 , 0.5, 5, "QuadEaseInOut"),
   (MIN_OUTPUT2 , 0.5, 5, "QuadEaseInOut"),
]

day_somebody_loops = 0

night_nobody_output1 = [
   (0, 1, 1, "LinearInOut"),
   (120, 3, 15, "LinearInOut"),
   (0, 3, 15, "LinearInOut"),
   (120, 3, 15, "LinearInOut"),

]

night_nobody_output2 = [
   (100, 1, 5, "QuadEaseInOut"),
   (0, 1, 5, "QuadEaseInOut"),
   (100, 1, 5, "QuadEaseInOut"),
   (0, 1, 5, "QuadEaseInOut")
]

night_nobody_loops = 0

night_somebody_output1 = [
   (120, 0.5, 1, "LinearInOut"),
   (0, 2, 1, "LinearInOut"),
]

night_somebody_output2 = [
   (100, 1, 5, "QuadEaseInOut"),
   (0, 3, 5, "QuadEaseInOut"),
   (100, 1, 5, "QuadEaseInOut"),
   (0, 2, 5, "QuadEaseInOut")
]

night_somebody_loops = 0

beautiful_output1 = [
   (120, 0.5, 1, "LinearInOut"),
   (0, 1, 1, "LinearInOut"),
   (120, 0.5, 1, "LinearInOut"),
   (0, 1, 1, "LinearInOut"),
   (120, 0.5, 1, "LinearInOut"),
   (0, 1, 1, "LinearInOut"),
]

beautiful_output2 = [
   (100, 0.5, 5, "QuadEaseInOut"),
   (0, 0.5, 5, "QuadEaseInOut"),
   (100, 0.5, 5, "QuadEaseInOut"),
   (0, 0.5, 5, "QuadEaseInOut"),
   (100, 0.5, 5, "QuadEaseInOut"),
   (0, 0.5, 5, "QuadEaseInOut"),
   (100, 0.5, 5, "QuadEaseInOut"),
   (0, 0.5, 5, "QuadEaseInOut"),
]

beautiful_loops = 1
