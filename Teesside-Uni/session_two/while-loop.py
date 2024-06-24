# Defining Variables
loop = 0 # Sets loop to have the value of 0.

# User Input
userInput =  int(input("Enter the times table you'd like to see: ")) # Retrieves a value from the user.

# Loops through code until the loop variable has a value that is 13 or above.
while loop < 13:
  print(loop, "times", userInput, "equals", loop * userInput) # Prints out the value of loop multiplied by userInput.
  loop = loop + 1 # Increments loop.