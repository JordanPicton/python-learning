# Importing Libs
import math

# Defining Variables
radius = float(input("Please input the radius of the circle to calculate the area: "))
pi = math.pi # Sets pi Variable using the math library as it has a function that already stores pi.

# Main Program
area = pi * (radius ** 2) # Calculates the area of a circle.
area = round(area, 3) # Rounds area to the third decimal place. 
diameter = radius * 2 # Calculates the diameter with simple Multiplication.
circumference = pi * diameter # Calculates the circumference with a simple Multiplication.

# Outputs
print("Area:", area, "Diameter:", diameter, "Circumference:", circumference) # Displays all the calculations relating the circle formula
