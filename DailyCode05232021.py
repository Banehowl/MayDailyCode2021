# --------------------------------------------------------
# #	Daily Code	05/23/2021
#   "Distance Between Two Points" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------

# In this challenge, you have to find the distance between two points placed on a Cartesian plane. Knowing the
# coordinates of both the points, you have to apply the Pythagorean theorem to find the distance between them.

# get_distance(-2, 1, 4, 3) -> 6.325

def get_distance(x1, y1, x2, y2):
    result = ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
    return result

print get_distance(-2, 1, 4, 3)