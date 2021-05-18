# ---------------------------------------------
# #	Daily Code	05/18/2021
#   "Shuffle the Name" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

# Create a function that takes a string (will be a person's first and last name) and returns a string with the
# first and last name swapped.

# name_shuffle("Donald Trump") -> "Trump Donald"
# name_shuffle("Rosie O'Donnell") -> "O'Donnell Rosie"
# name_shuffle("Seymour Butts") -> "Butts Seymour"

def name_shuffle(txt):
    stringTxt = str(txt)
    arrayTxt = stringTxt.split()
    reverseTxt = reversed(arrayTxt)
    spaceTxt = " "
    joinTxt = spaceTxt.join(reverseTxt)
    return joinTxt

print name_shuffle("Donald Trump")
print name_shuffle("Rosie O'Donnell")
print name_shuffle("Seymour Butts")