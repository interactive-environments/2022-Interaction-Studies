# Varspeed declarations
MIN_OUTPUT1 = 1
MAX_OUTPUT1 = 20
MIN_OUTPUT2 = 0
MAX_OUTPUT2 = 360
NOBODY_OUTPUT2 = 30
BEAUTIFUL_OUTPUT2 = 359
#LED_MIN_OUTPUT3 = (0,0,0)
#LED_MAX_OUTPUT3 = (255,255,255)

# Behaviour sequences
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
day_nobody_output1 = [
   (MAX_OUTPUT1, 1, 50, "LinearInOut"),
   (MIN_OUTPUT1, 1, 50, "LinearInOut"),
   (MAX_OUTPUT1, 1, 50, "LinearInOut"),
   (MIN_OUTPUT1, 1, 50, "LinearInOut"),
   (MAX_OUTPUT1, 1, 50, "LinearInOut"),
   (MIN_OUTPUT1, 1, 50, "LinearInOut"),
]

day_nobody_output2 = [
   (NOBODY_OUTPUT2, 2, 50, "QuadEaseInOut"),
   (MIN_OUTPUT2, 2, 50, "QuadEaseInOut")
]

#day_nobody_output3 = [
 #  (LED_MAX_OUTPUT3, 2, 50, "QuadEaseInOut"),
  # (LED_MIN_OUTPUT3, 2, 50, "QuadEaseInOut")
#]

day_nobody_loops = 0

day_somebody_output1 = [
   (100, 2, 100, "LinearInOut"),
   (0, 2, 100, "LinearInOut"),
]

day_somebody_output2 = [
   (MAX_OUTPUT2, 2, 80, "QuadEaseInOut"),
   (MIN_OUTPUT2, 2, 80, "QuadEaseInOut")
]

day_somebody_loops = 0

night_nobody_output1 = [
   (0, 1.5, 50, "LinearInOut"),
   (20, 1.5, 50, "LinearInOut"),
]

night_nobody_output2 = [
   (NOBODY_OUTPUT2, 2, 50, "QuadEaseInOut"),
   (MIN_OUTPUT2, 2, 50, "QuadEaseInOut")
]

night_nobody_loops = 0

night_somebody_output1 = [
   (0, 1.0, 1, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (0, 10.0, 11, "LinearInOut")
]

night_somebody_output2 = [
   (MAX_OUTPUT2, 2, 80, "QuadEaseInOut"),
   (MIN_OUTPUT2, 2, 80, "QuadEaseInOut")
]

night_somebody_loops = 0

beautiful_output1 = [
   (0, 1.0, 1, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (10, 0.1, 2, "LinearInOut"),
   (0, 0.1, 2, "LinearInOut"),
   (0, 10.0, 11, "LinearInOut")
]

beautiful_output2 = [
   (BEAUTIFUL_OUTPUT2, 2, 80, "QuadEaseInOut"),
   (MIN_OUTPUT2, 2, 80, "QuadEaseInOut")
]

beautiful_loops = 1

