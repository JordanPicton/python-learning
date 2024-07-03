# Simple Comparison Program
# Jordan Picton 01/07/2024

# Delcaring variables using input statements. Casts those values to integers.
inputOne = int(input("Enter a number: "))
inputTwo = int(input("Enter another number: "))

# Compare Program.
if inputOne > inputTwo: # Checks if inputOne is bigger than inputTwo
  print(inputOne, "is the biggest!")  # Prints out inputOne is the biggest if the condition above is true.
elif inputTwo > inputOne: # If the condition before was false then do this next condition. Is inputTwo bigger than inputOne.
  print(inputTwo, "is the biggest!") # Print out that inputTwo is biggest if the condition above is true.
else: # If anything else then run the code below.
  print("Both are equal!") # Print out that "Both are equal."