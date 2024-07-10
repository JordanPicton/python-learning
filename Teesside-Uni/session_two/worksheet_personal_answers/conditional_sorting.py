# Conditional Sorting Program
# Jordan Picton 03/07/2024

flag = True

# Declare variables
numList = []  # Creating a new empty list.

numOne = input(
    "Please insert your delivery weight here or 'exit' to quit the program: ")
numList.append(int(numOne))# Adds the value from numOne into the numList list.

print(numList)

while flag:
      # Takes user input to give the variable a value.
      numOne = input("Please insert your next delivery weight here or 'exit' to quit the program: ")
      numList.append(int(numOne))# Adds the value from numOne into the numList list.
      # Checks if the value of
      if numOne == "exit":
        flag = False
      else:
        numList.append(int(numOne))# Adds the value from numOne into the numList list.
        numOne = input("Please insert your next delivery weight here or 'exit' to quit the program: ")
        if numOne == "exit":
          flag = False
          print(numList)
          
numList.sort()
print(numList)