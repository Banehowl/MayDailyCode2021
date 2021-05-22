# ---------------------------------------------------
# #	Daily Code	05/22/2021
#   "Hiding the Card Number" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------

# Write a function that takes a credit card number and only displays the last four characters.
# The rest of the card number must be replaced by ************.

# card_hide("1234123456785678") -> "************5678"
# card_hide("8754456321113213") -> "************3213"
# card_hide("35123413355523") -> "**********5523"

def card_hide(card):
    cardCount = len(card)
    omitNumbers = cardCount - 4
    sliceNumber = card[omitNumbers:]
    replaceNumbers = "*" * omitNumbers
    output = replaceNumbers + sliceNumber
    return output

print card_hide("1234123456785678")
print card_hide("8754456321113213")
print card_hide("35123413355523")