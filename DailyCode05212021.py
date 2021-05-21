# ---------------------------------------------
# #	Daily Code	05/21/2021
#   "How Many Vowels?" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

# Create a function that takes a string and returns the number (count) of vowels contained within it.

# count_vowels("Celebration") -> 5
# count_vowels("Palm") -> 1
# count_vowels("Prediction") -> 4

def count_vowels(txt):
    strTxt = str(txt)
    volCountA = strTxt.count('a')
    volCountE = strTxt.count('e')
    volCountI = strTxt.count('i')
    volCountO = strTxt.count('o')
    volCountU = strTxt.count('u')
    countTotal = volCountA + volCountE + volCountI + volCountO + volCountU
    return countTotal

print count_vowels("Celebration")
print count_vowels("Palm")
print count_vowels("Prediction")