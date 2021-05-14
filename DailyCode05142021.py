# -----------------------------------------------------
# #	Daily Code	05/14/2021
#   "Correct Inequality Signs" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------------

# Create a function that returns True if a given inequality expression is correct and False otherwise.

# correct_signs("3 < 7 < 11") -> True
# correct_signs("13 > 44 > 33 > 1") -> False
# correct_signs("1 < 2 < 6 < 9 > 3") -> True

def correct_signs(x,y):
    if x > y:
        return True
    else:
        return False