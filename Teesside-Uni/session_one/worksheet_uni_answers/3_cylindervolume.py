# import math module for access to pi
import math

# Get input from the user
r = float(input("Enter radius of cylinder: "))
h = float(input("Enter the height of the cylinder: "))

# pi * radius^2 * height - formula for the volume of a cylinder
# Perform the calculation and store in variable volume.
volume = math.pi * r**2 * h

# Output the result
print("The volume of the cylinder is", volume)