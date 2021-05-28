# -----------------------------------------------------------
# #	Daily Code	05/27/2021
#   "Convert Age to Days (one line)" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------------------

# Create a function that takes the age in years and returns the age in days.

# calc_age(65) -> 23725
# calc_age(0) -> 0
# calc_age(20) -> 7300

def calc_age(num):
    return num * 365

print calc_age(65)
print calc_age(0)
print calc_age(20)