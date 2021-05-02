# ---------------------------------------
# #	Daily Code	05/05/2021
#   "Roll a dXX" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------

# Create code that rolls a d20, d4, d6, d8, d10, d12, d00

import random

dice_20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dice_4 = [1, 2, 3, 4]
dice_6 = [1, 2, 3, 4, 5, 6]
dice_8 = [1, 2, 3, 4, 5, 6, 7, 8]
dice_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dice_12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dice_00 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 00]

print(random.choice(dice_20))
print(random.choice(dice_4))
print(random.choice(dice_6))
print(random.choice(dice_8))
print(random.choice(dice_10))
print(random.choice(dice_12))
print(random.choice(dice_00))
