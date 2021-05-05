# --------------------------------------------------------
# #	Daily Code	05/05/2021
#   "Convert Kilometers to Miles" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------

# In this challenge, you have to implement a function that returns the given distance kilometers converted into miles.

# km_to_miles(2) -> 1.24274
# km_to_miles(6) -> 3.72823
# km_to_miles(8) -> 4.97097

def km_to_miles(n):
    convertToMile = n * .621371
    return convertToMile

print km_to_miles(2)
print km_to_miles(6)
print km_to_miles(8)