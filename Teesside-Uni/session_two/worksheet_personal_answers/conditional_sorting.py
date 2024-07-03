# Conditional Sorting Program
# Jordan Picton 03/07/2024

# Declare variables. (User inputs)
# numOne = int(input("Please insert your first number: ")) # Takes user input to give the variable a value.
# numTwo = int(input("Please insert your second number: ")) # Takes user input to give the variable a value.
# numThree = int(input("Please insert your third number: ")) # Takes user input to give the variable a value.

flag = True

# Declare variables
numList = []  # Creating a new empty list.

numOneList = input(
    "Please insert your third number or 'exit' to quit the program: ")

while flag:
      # Takes user input to give the variable a value.
      numOne = input("Please insert your first number or 'exit' to quit the program: ")
      # Checks if the value of
      if numOne == "exit":
        flag = False
      else:
        numList.append(int(numOne))# Adds the value from numOneList into the numList list.
        numTwo = input("Please insert your second number or 'exit' to quit the program: ")
        if numTwo == "exit":
          print(numList)