# ------------------------------------------------
# #	Daily Code	05/05/2021
#   "Stuttering Function" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------

# Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated
# twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

# stutter("incredible") -> "in... in... incredible?"
# stutter("enthusiastic") -> "en... en... enthusiastic?"
# stutter("outstanding") -> "ou... ou... outstanding?"

def stutter(word):
    sliceObj = slice(0,2)
    sliceWord = word[sliceObj]
    stutterSentence = sliceWord + "... " + sliceWord + "... " + word
    return stutterSentence

print stutter("incredible")
print stutter("enthusiastic")
print stutter("outstanding")