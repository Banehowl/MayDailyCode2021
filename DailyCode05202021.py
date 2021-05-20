# ---------------------------------------------
# #	Daily Code	05/20/2021
#   "How Heavy Is It?" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

# Given radius r and height h (in cm), calculate the mass of a cylinder when it's filled with water and the cylinder
# itself doesn't weigh anything. The desired output should be given in kg and rounded to two decimal places.

def weight(r, h):
    piMath = 3.14
    circleArea = piMath * r ** 2
    volumeCylinder = circleArea * h
    return volumeCylinder

print weight(4, 10)
print weight(30, 60)
print weight(15, 10)