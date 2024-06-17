# Import math so we can use pi
import math

# Read in the user input
r1 = float(input("Please enter first radius: ")) # Condensed version of reading and converting input
r2 = float(input("Please enter second radius: ")) 

# pi * radius_1 * radius_2 - formula for the area of an ellipse
# Performs calculation and stores in the variable area
area = math.pi * r1 * r2

# Output the result of the calculation
print("Area of the ellipse is", area)