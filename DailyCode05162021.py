# --------------------------------------------------------------
# #	Daily Code	05/15/2021
#   "Xs and Os, Nobody Knows (level 2)" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------

# Create a function that takes a string, checks if it has the same number of "x"s and "o"s and
# returns either True or False.

# Return a boolean value (True or False).
# Return True if the amount of x's and o's are the same.
# Return False if they aren't the same amount.

# XO("ooxx") -> True
# XO("xooxx") -> False
# XO("XoXo") -> False
# XO("XXxxOOoo") -> True

def XO(txt):
    subStringx = "x"
    subStringo = "o"
    subStringX = "X"
    subStringO = "O"
    countX = txt.count(subStringx)
    countO = txt.count(subStringo)
    countXX = txt.count(subStringX)
    countOO = txt.count(subStringO)
    if countX == countO & countXX == countOO:
        return True
    else:
        return False

print XO("ooxx")
print XO("xooxx")
print XO("XoXo")
print XO("XXxxOOoo")
