# ------------------------------------------------------
# #	Daily Code	05/03/2021
#   "Among Us Imposter Formula" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------------

# Create a function that calculates the chance of being an imposter. The formula for the chances of being an imposter
# is 100 * (i / p) where i is the imposter count and p is the player count. Make sure to round the value to the nearest
# integer and return the value as a percentage.

def imposter_formula(i, p):
    impOdds = 100 * (i/p)
    return impOdds

print imposter_formula(1, 10)
print imposter_formula(2, 5)
print imposter_formula(1, 8)