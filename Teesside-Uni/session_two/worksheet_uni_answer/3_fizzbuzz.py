# A classic programming test question. Make sure you've
#  given this one a go yourself!
# As a reminder: % operator is the modulus operator - 
#  it will return the remainder when you divide the first
#  argument by the second
# 10 % 5 returns 0, 11 % 5 returns 1

# Get input from user
x = int(input("Enter a number: "))


# Note the order of these conditions - you must check the 
#  most complex condition first, as an if statement will 
#  always take the first valid path.
# If you check divisibility with 3 or 5 first, it will
#  always be followed over the more complex check.

# Checks if x is divisible by both 3 and 5
if (x % 3 == 0) and (x % 5 == 0):
    print("FizzBuzz")
# Checks if x is divisible by 3
elif (x % 3 == 0):
    print("Fizz")
# Checks if x is divisible by 5
elif (x % 5 == 0):
    print("Buzz")
# x is not divisible by 3 and 5
else:
    print(x)