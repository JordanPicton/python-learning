# FizzBuzz Program
# Jordan Picton 03/07/2024

# Declaring Variables.
inputNumber = int(input("Please insert a number: "))

# Main program.
if (inputNumber % 3 == 0) and (inputNumber % 5 == 0): # Check if the value of inputNumber divided by 3 is equal to 0 remainder AND if the value of inputNumber divided by 5 is equal to 0 remainder.
  print("FizzBuzz") # Print out FizzBuzz
elif inputNumber % 3 == 0: # Check if the value of inputNumber divided by 3 is equal to 0 remainder.
  print("Fizz") # Print out Fizz
elif inputNumber % 5 == 0: # Check if the value of inputNumber divided by 5 is equal to 0 remainder.
  print("Buzz") # Print out Buzz
else: # For anything else run the code below.
  print(inputNumber) # Prints out the value of inputNumber.