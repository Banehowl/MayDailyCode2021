# -------------------------------------------------
# #	Daily Code	05/11/2021
#   "Return the Factorial" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------

# Create a function that takes an integer and returns the factorial of that integer. That is, the integer
# multiplied by all positive lower integers.

# factorial(3) -> 6
# factorial(5) -> 120
# factorial(13) -> 6227020800

import math

def factorial(num):
    solution = math.factorial(int(num))
    return solution

print factorial(3)
print factorial(5)
print factorial(13)