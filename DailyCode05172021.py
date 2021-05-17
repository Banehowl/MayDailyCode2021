# ---------------------------------------
# #	Daily Code	05/17/2021
#   "Am I Sick?" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------

# Create code that spits out a diagnosis

def AmISick(txt):
    if txt == "yes":
        return "That's a Shame"
    elif txt == "no":
        return "No, you're actually sick. Sorry!"

print AmISick("yes")
print AmISick("no")