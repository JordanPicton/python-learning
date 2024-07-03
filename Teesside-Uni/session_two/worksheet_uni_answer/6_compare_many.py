# Solution uses the same if-elif-else construct as 
#  the original comparison code. If you need more 
#  explanation, look at that solution first.

# We want to create a program that performs the 
#  comparison until the user enters "quit".
# Since there is no limit on the amount of times
#  we will compare the code, we should use a while
#  loop!

# There are many ways to set up this kind of loop.
# In this example, I am using a "flag" - a boolean
#  variable that is used to determine when the loop
#  should keep going and when it should stop.
# These kind of variables need to be created before 
#  the loop starts.
flag = True

# Create a while loop using the flag as the condition
# As the flag is a boolean value already, this condition
#  is the same as flag == True
while flag: 
    # Read user input as a string
    x = input("Enter the first number, or quit to exit: ")

    #Perform the check before the input is converted
    if x == "quit":
        # User has entered "quit" - stop the loop
        flag = False 
    else:
        # x is not "quit" - get the second number
        # y is also read in as a string in case the user
        #  enters quit second
        y = input("Enter the second number, or quit to exit: ")

        # Check to see if quit was entered
        if y == "quit":
            # User entered "quit", end the loop
            flag = False
        else:
            # Both x and y are not quit - user wants to compare numbers
            # Convert both x and y strings to int
            x = int(x)
            y = int(y)

            # Compare the two numbers
            if x > y:
                print(x, "is greather than", y)
            elif x < y:
                print(x, "is less than", y)
            else:
                print("Both numbers are equal!")
