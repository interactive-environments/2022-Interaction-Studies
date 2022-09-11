
# Varspeed declarations
MIN_OUTPUT1 = 0
MAX_OUTPUT1 = 200
MIN_OUTPUT2 = 0
MAX_OUTPUT2 = 180

# Behaviour sequences
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net

day_nobody_output1 = [
    (MAX_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MIN_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MAX_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MIN_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MAX_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MIN_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MAX_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MIN_OUTPUT1, 0.1, 5, "LinearInOut"),
]

day_nobody_output2 = [
    (MAX_OUTPUT2, 3, 50, "QuadEaseInOut"),
    (MIN_OUTPUT2, 3, 50, "QuadEaseInOut"),
    (MAX_OUTPUT2, 3, 50, "QuadEaseInOut"),
    (MIN_OUTPUT2, 3, 50, "QuadEaseInOut"),
    (MAX_OUTPUT2, 3, 50, "QuadEaseInOut"),
    (MIN_OUTPUT2, 3, 50, "QuadEaseInOut"),
]

day_nobody_loops = 0

day_somebody_output1 = [
    (MAX_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MAX_OUTPUT1, 0.3, 5, "LinearInOut"),
    (MIN_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MAX_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MAX_OUTPUT1, 0.3, 5, "LinearInOut"),
    (MIN_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MAX_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MAX_OUTPUT1, 0.3, 5, "LinearInOut"),
    (MIN_OUTPUT1, 0.1, 5, "LinearInOut"),
]

day_somebody_output2 = [
    (MAX_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MIN_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MAX_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MIN_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MAX_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MIN_OUTPUT2, 1, 100, "BounceEaseInOut"),
]

day_somebody_loops = 0

# What is everybody?
day_everybody_output1 = [
    (MAX_OUTPUT1, 0.1, 5, "LinearInOut"),
    (MAX_OUTPUT1, 1, 5, "LinearInOut"),
]

day_everybody_output2 = [
    (MAX_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MIN_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MAX_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MIN_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MAX_OUTPUT2, 1, 100, "BounceEaseInOut"),
    (MIN_OUTPUT2, 1, 100, "BounceEaseInOut"),
]

night_nobody_output1 = [
    (MAX_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.8, 20, "LinearInOut"),
    (MAX_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.8, 20, "LinearInOut"),
    (MAX_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.8, 20, "LinearInOut"),
    (MAX_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.2, 20, "LinearInOut"),
]

night_nobody_output2 = [
    (MAX_OUTPUT2, 5, 100, "QuadEaseInOut"),
    (MIN_OUTPUT2, 5, 100, "QuadEaseInOut"),
    (MAX_OUTPUT2, 5, 100, "QuadEaseInOut"),
    (MIN_OUTPUT2, 5, 100, "QuadEaseInOut"),
    (MAX_OUTPUT2, 5, 100, "QuadEaseInOut"),
    (MIN_OUTPUT2, 5, 100, "QuadEaseInOut"),
]

night_nobody_loops = 0

night_somebody_output1 = [
    (MAX_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MAX_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MAX_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MAX_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MIN_OUTPUT1, 0.2, 20, "LinearInOut"),
]

night_somebody_output2 = [
    (MAX_OUTPUT2, 3, 100, "QuadEaseInOut"),
    (MIN_OUTPUT2, 3, 100, "QuadEaseInOut"),
    (MAX_OUTPUT2, 3, 100, "QuadEaseInOut"),
    (MIN_OUTPUT2, 3, 100, "QuadEaseInOut"),
    (MAX_OUTPUT2, 3, 100, "QuadEaseInOut"),
    (MIN_OUTPUT2, 3, 100, "QuadEaseInOut"),
]

night_somebody_loops = 0

beautiful_output1 = [
    (MAX_OUTPUT1, 0.2, 20, "LinearInOut"),
    (MAX_OUTPUT1, 2, 20, "LinearInOut"),
    (MIN_OUTPUT1, .2, 20, "LinearInOut"),
]

beautiful_output2 = [
    (MAX_OUTPUT2, 1, 100, "QuadEaseInOut"),
    (MIN_OUTPUT2, 1, 100, "QuadEaseInOut"),
    (MAX_OUTPUT2, 1, 100, "QuadEaseInOut"),
    (MIN_OUTPUT2, 1, 100, "QuadEaseInOut"),
    (MAX_OUTPUT2, 1, 100, "QuadEaseInOut"),
    (MIN_OUTPUT2, 1, 100, "QuadEaseInOut"),
]

beautiful_loops = 1
