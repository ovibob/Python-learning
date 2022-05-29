import random
import sys
import time


width = 70
pause_amount = 5


print('Press Ctrl-C to stop!')
time.sleep(2)

gap_width = 10
left_width = 25

while True:
    # display the tunnel segment
    right_width = width - gap_width - left_width
    print(('#' * left_width) + (' ' * gap_width) + ('#' * right_width))

    # check for Ctrl-C press during the brief pause:
    try:
        time.sleep(pause_amount)
    except KeyboardInterrupt:
        sys.exit() # when Ctrl - C is pressed end the program

    # adjust the left side width
    dice_roll = random.randint(1,6)
    if dice_roll == 1 and left_width > 1:
        left_width = left_width - 1 # decrease left side width
    elif dice_roll == 2 and left_width + gap_width < width - 1:
        left_width = left_width + 1 # increase the left side width
    else:
        pass # do nothing; no change in left side width



