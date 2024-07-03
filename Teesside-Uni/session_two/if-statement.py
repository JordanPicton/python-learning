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

# Age verifification IF Statement.
age = int(input("Enter your age: ")) # Declaring variable with user input which is casted to an integer.
if age < 18: # Checks if the value of age is less than 18.
  adult = input("Do you have an adult with you?").lower() # Declares a variable with user input that uses the lower() method.
  if adult != "yes": # Checks if the answer give from the variable created above has the anything other than "yes".
    # If anything other than yes is given then continue running the code within this block.
    print("Access Denied!") # Print out Access Denied message.
    exit(0) # Exit the program. (Skips the rest of the code below for this if Statement.) This part is interesting.
  else: # If the answer is yes then continue with the code below.
    print("You can proceed.") # Print out You can proceed.