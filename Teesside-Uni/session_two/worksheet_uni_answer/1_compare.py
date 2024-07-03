# Solution to compare two numbers
# There's more comments than usual here, so extra spaces
#  are included to help you read the code and comments 
#  together.

# Gather input from the user.
# Converted to int so they can be compared effectively
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# if-elif-else block to compare the numbers
# First check is if x is the larger number. 
# We must use >, as equal numbers need a 
#  different output
if x > y: 
    # x > y is True - execute this block of code
    print(x, "is greather than", y)

# elif. We only reach this point if x > y is False,
#  so we know that x is less than y or x is equal to y.
# As before, we need to use < as equality still needs a
#  different output.
elif x < y:
    # x < y is True - execute this block of code
    print(x, "is less than", y)

# else. This block is only reached if none of the previous
#  conditions are True. In this case, this means that the 
#  else branch will only be reached if x < y is False and 
#  x > y is False.
# This will only happen if x and y are equal, so we don't need 
#  another check - we can just use else.
else:
    print("Both numbers are equal!")