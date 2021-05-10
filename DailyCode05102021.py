# ------------------------------------------------
# #	Daily Code	05/10/2021
#   "Basic Calculator (again)" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------

# Create a function that takes two numbers and a mathematical operator + - / * and will perform a
# calculation with the given numbers.

# calculator(2, "+", 2) -> 4
# calculator(2, "*", 2) -> 4
# calculator(4, "/", 2) -> 2

def calculator(num, operator, num2):
    solution = 0
    if operator == "+":
        solution = num + num2
    elif operator == "-":
        solution = num - num2
    elif operator == "*":
        solution = num * num2
    elif operator == "/":
        if num2 == 0:
            return "Can't Divide by 0!"
        else:
            solution = num / num2
    return solution

print calculator(2, "+", 2)
print calculator(2, "*", 2)
print calculator(4, "/", 2)
print calculator(4, "/", 0)