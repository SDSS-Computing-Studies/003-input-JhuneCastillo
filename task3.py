#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
import math

a = input('Enter value of "a": ')
b = input('Enter value of "b": ')
c = input('Enter value of "c": ')

a2 = int(a)
b2 = int(b)
c2 = int(c)

result = ((c2 - b2) / a2)

y = str(result)

print("x = " + y)
