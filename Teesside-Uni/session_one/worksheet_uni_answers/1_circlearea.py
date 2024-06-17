# Lines of code starting with a # symbol are ignored by the Python
#  interpreter. These "comments" are very useful to explain or describe code and
#  will help others understand what you have written.
# These examples will include comments to help explain the solutions or point out
#  useful techniques and structures.

# We know that we will need to use pi, so we will import the math module to use
#  the built-in constant.
import math

# Prompt the user to enter a radius and store the input in r.
r = input("Please enter the radius: ")
r = float(r) # Converts the input to a number - int or float both work for this question.

# pi * radius^2 - formula for the area of a circle.
# Calculates result and stores in the variable area.
area = math.pi * r ** 2 

# 2*pi*r - formula for the circumference of a circle.
# Calculates result and stores in the variable circumference.
circumference = math.pi * 2 * r

# Output the result of the calculation.
print("Area of the circle is", area)
print("Circumference of the circle is", circumference)
