#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704

import math

side1 = input("Enter value for First side: ")
side2 = input("Enter value for Second side: ")

side1 = int(side1)
side2 = int(side2)

result = math.hypot(side1, side2)
x = str(result)

print("The hypotenuse has a length of " + x)
