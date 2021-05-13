# -------------------------------------------------------------
# #	Daily Code	05/13/2021
#   "Is it Time for Milk and Cookies?" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------------

# Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function
# that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.

# time_for_milk_and_cookies(datetime.date(2013, 12, 24)) -> True
# time_for_milk_and_cookies(datetime.date(2013, 1, 23)) -> False
# time_for_milk_and_cookies(datetime.date(3000, 12, 24)) -> True

import datetime

def time_for_milk_and_cookies(date):
    if date == datetime.date( 2000,12,24):
        return True
    else:
        return False