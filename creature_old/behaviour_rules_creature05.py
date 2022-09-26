MIN_OUTPUT1 = 5
MAX_OUTPUT1 = 255
MIN_OUTPUT2 = 0
MAX_OUTPUT2 = 230

# Behaviour sequences
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
day_nobody_output1 = [
   (20, 7, 100, "BounceEaseIn"),
   (1, 7, 100, "BounceEaseOut"),
]

# BounceOut - is not known?!
day_nobody_output2 = [
   (MIN_OUTPUT2, 2, 100,"BounceOut"),
   (MAX_OUTPUT2, 2, 100,"BounceInt"),
]

day_nobody_loops = 0

day_somebody_output1 = [
   (20, 1, 1, "LinearInOut"),
   (0, 1, 1, "LinearInOut"),
]

day_somebody_output2 = [
   (MIN_OUTPUT2, 0.5, 1,"LinearInOut"),
   (MAX_OUTPUT2, 0.5, 1,"LinearInOut"),
]

day_somebody_loops = 0

night_nobody_output1 = [
  (200, 3, 100, "BounceEaseIn"),
   (5, 3, 100, "BounceEaseOut"),
]

night_nobody_output2 = [
   (MIN_OUTPUT2, 0.75, 100,"BounceOut"),
   (MAX_OUTPUT2, 0.75, 100,"BounceInt"),
]

night_nobody_loops = 0

night_somebody_output1 = [
    (255, 0.3, 10, "LinearInOut"),
    (5, 0.3, 10, "LinearInOut"),
]

night_somebody_output2 = [
   (MIN_OUTPUT2, 0.2, 1,"LinearInOut"),
   (MAX_OUTPUT2, 0.2, 1,"LinearInOut"),
]

night_somebody_loops = 0

beautiful_output1 = [
   (255, 0.1, 10, "LinearInOut"),
    (5, 0.1, 10, "LinearInOut"),
]

beautiful_output2 = [
   (MIN_OUTPUT2, 0.05, 1,"LinearInOut"),
   (MAX_OUTPUT2, 0.05, 1,"LinearInOut"),
]

beautiful_loops = 1

