# Collecting inputs from user.
inputOne = int(input("Enter a number: "))
inputTwo = int(input("Enter another number: "))

# Simple Elif Statement
if inputOne > inputTwo: # Checks if inputOne is bigger than inputTwo
  print(inputOne, "is the biggest!")  # Prints out inputOne is the biggest if the condition above is true.
elif inputTwo > inputOne: # If the condition before was false then do this next condition. Is inputTwo bigger than inputOne.
  print(inputTwo, "is the biggest!") # Print out that inputTwo is biggest if the condition above is true.
else: # If anything else then run the code below.
  print("Both are equal!") # Print out that "Both are equal."

# Slightly more complex IF statement
numberOne = int(input("Enter a number more than 100, and even (No decimals): ")) # Variable Delcaration 

# If statement checks if the value stored within numberOne is greater than 100.
if numberOne > 100 and numberOne % 2 == 0:
  print(numberOne, "is a very cool number!") # Prints out that this is a cool number.
else:
 print(numberOne, "is a very uncool number.") # Prints out that this is an uncool number.