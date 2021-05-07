# -----------------------------------------------
# #	Daily Code	05/07/2021
#   "Radians to Degrees" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------

# Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded
# to one decimal place.

# radians_to_degrees(1) -> 57.3
# radians_to_degrees(20) -> 1145.9
# radians_to_degrees(50) -> 2864.8

import math

def radians_to_degrees(num):
    piMath = math.pi
    convertRads = num * (180/piMath)
    roundAnswer = round(convertRads, 1)
    return roundAnswer

print radians_to_degrees(1)
print radians_to_degrees(20)
print radians_to_degrees(50)