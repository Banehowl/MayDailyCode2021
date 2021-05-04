# --------------------------------------------
# #	Daily Code	05/03/2021
#   "Drinks Allowed?" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------

# A bartender is writing a simple program to determine whether he should serve drinks to someone.
# He only serves drinks to people 21 and older and when he's not on break.
#
# Given the person's age, and whether break time is in session, create a function which returns whether he
# should serve drinks.

# should_serve_drinks(17, True) -> False
# should_serve_drinks(21, False) -> True
# should_serve_drinks(30, True) -> False

def should_serve_drinks(age, on_break):
    if age >= 21 & on_break == False:
        return True
    else:
        return False

print should_serve_drinks(17, True)
print should_serve_drinks(21, False)
print should_serve_drinks(30, True)