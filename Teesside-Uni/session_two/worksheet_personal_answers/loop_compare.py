# Loop Compare Program
# Jordan Picton 04/07/2024

# Declare a Boolean Value
flag = True

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
  
while flag:
    inputOne = input("Enter a number or type 'exit' to quit the program: ")
    inputTwo = input("Enter another number or type 'exit' to quit the program: ")
    if inputOne.lower() == "exit" or inputTwo.lower() == "exit":
        flag = False
        print("You have quit the program!")
    else:
        inputOne = int(inputOne)
        inputTwo = int(inputTwo)
        if inputOne > inputTwo: # Checks if inputOne is bigger than inputTwo
            print(inputOne, "is the biggest!")  # Prints out inputOne is the biggest if the condition above is true.
        elif inputTwo > inputOne: # If the condition before was false then do this next condition. Is inputTwo bigger than inputOne.
            print(inputTwo, "is the biggest!") # Print out that inputTwo is biggest if the condition above is true.
        else: # If anything else then run the code below.
            print("Both are equal!") # Print out that "Both are equal."