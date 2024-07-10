# Conditional Sorting Program
# Jordan Picton 03/07/2024

# Declare a Boolean Variable
flag = True

# Declare an empty list.
numList = []  # Creating a new empty list.

# Retrieving input from the user.
numOne = input("Please insert your delivery weight here: ")
if numOne.lower() != "exit": # Checks to make sure the value IS NOT TRUE.
    numList.append(int(numOne)) # Add the value to the list.
    print(numList)  # Prints the value of the numList for testing.

while flag:  # Whilst True do the following:
    # Takes user input to give the variable a value.
    numOne = input("Please insert your next delivery weight here or 'exit' to quit the program: ")
    if numOne.lower() == "exit": # Checks if the value is equal to exit if it is then run the code below:
        flag = False # Stops the loop.
        numList.sort() # Sorts the values within the list.
        print(numList) # Prints out the list to console.
    else: # If the value is not equal to exit then continue with the code below:
        numList.append(int(numOne)) # Add the value to the list.
        numList.sort()  # Sort the list.
        print(numList)  # Print out the new order of the list.