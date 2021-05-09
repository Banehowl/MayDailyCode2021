# ------------------------------------------------
# #	Daily Code	05/09/2021
#   "Luke, I Am Your ..." Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------

# Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name,
# return the relation of that person to Luke.

# Person	    Relation
# Darth Vader	father
# Leia	        sister
# Han	        brother in law
# R2D2	        droid

# relation_to_luke("Darth Vader") -> "Luke, I am your father."
# relation_to_luke("Leia") -> "Luke, I am your sister."
# relation_to_luke("Han") -> "Luke, I am your brother in law."

def relation_to_luke(name):
    if name == "Darth Vader":
        return "Luke, I am your father"
    elif name == "Leia":
        return "Luke, I am your sister"
    elif name == "Han":
        return "Luke, I am your brother in law"
    elif name == "R2D2":
        return "Luke, I am your droid"

print relation_to_luke("Darth Vader")
print relation_to_luke("Leia")
print relation_to_luke("Han")
print relation_to_luke("R2D2")