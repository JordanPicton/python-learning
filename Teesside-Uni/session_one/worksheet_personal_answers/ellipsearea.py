# Importing Libs
import math

# Variables
pi = math.pi

# Main Program
userInOne = float(input("Please enter the first radius: "))
userInTwo = float(input("Please enter the second radius: "))

# Uses pi and then multiplies the two other inputs
area = pi * userInOne * userInTwo

# Output
print("The area of the ellipse is:", area)