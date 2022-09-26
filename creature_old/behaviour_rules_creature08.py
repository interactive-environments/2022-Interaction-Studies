
# Varspeed declarations
MIN_OUTPUT1 = 0
MAX_OUTPUT1 = 200
MIN_OUTPUT2 = 0
MAX_OUTPUT2 = 180

# Behaviour sequences
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
day_nobody_output1 = [
   (99, 3, 5, "LinearInOut"),
   (MAX_OUTPUT1, 0.5, 5, "LinearInOut"),
   (99, 0.5, 5, "LinearInOut"),
   (MIN_OUTPUT1, 3, 5, "LinearInOut"),
]

day_nobody_output2 = [
    (MAX_OUTPUT2, 0.3, 10, "LinearInOut"),
    (MIN_OUTPUT2, 0.3, 10, "LinearInOut")
    #(90, 5, 10, "QuadEaseInOut"),
   #(MAX_OUTPUT2, 5, 20, "QuadEaseInOut"),
   #(90, 5, 10, "QuadEaseInOut"),
   #(MIN_OUTPUT2, 5, 20, "QuadEaseInOut")
]
day_nobody_loops = 0

day_somebody_output1 = [
   (99, 0.01, 5, "LinearInOut"),
   (MAX_OUTPUT1, 1, 5, "LinearInOut"),
   (99, 1, 5, "LinearInOut"),
   (MIN_OUTPUT1, 0.01, 5, "LinearInOut")
]

day_somebody_output2 = [
    (MAX_OUTPUT2, 0.1, 4, "LinearInOut"),
    (MIN_OUTPUT2, 0.1, 4, "LinearInOut")
   #(90, 3, 10, "QuadEaseInOut"),
   #(MAX_OUTPUT2, 3, 20, "QuadEaseInOut"),
   #(90, 3, 10, "QuadEaseInOut"),
   #(MIN_OUTPUT2, 3, 20, "QuadEaseInOut")
]

day_somebody_loops = 0

night_nobody_output1 = [
   (99, 5, 5, "LinearInOut")
]

night_nobody_output2 = [
   (90, 10, 20, "QuadEaseInOut"),
   (MAX_OUTPUT2, 10, 30, "QuadEaseInOut"),
   (90, 10, 10, "QuadEaseInOut"),
   (MIN_OUTPUT2, 10, 30, "QuadEaseInOut")
]

night_nobody_loops = 0

night_somebody_output1 = [
   (MAX_OUTPUT1, 0.1, 5, "LinearInOut"),
   (MIN_OUTPUT1, 0.1, 5, "LinearInOut")
]

night_somebody_output2 = [
   (90, 7, 10, "QuadEaseInOut"),
   (MAX_OUTPUT2, 7, 20, "QuadEaseInOut"),
   (90, 7, 10, "QuadEaseInOut"),
   (MIN_OUTPUT2, 7, 20, "QuadEaseInOut")
]

night_somebody_loops = 0

beautiful_output1 = [
   (99, 0.05, 5, "LinearInOut"),
   (MAX_OUTPUT1, 2, 5, "LinearInOut"),
   (99, 2, 5, "LinearInOut"),
   (MIN_OUTPUT1, 0.05, 5, "LinearInOut")
]

beautiful_output2 = [
   (90, 3, 10, "QuadEaseInOut"),
   (MAX_OUTPUT2, 3, 20, "QuadEaseInOut"),
   (90, 3, 10, "QuadEaseInOut"),
   (MIN_OUTPUT2, 3, 20, "QuadEaseInOut")
]
beautiful_loops = 1
