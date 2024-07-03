# Now that we are using control-flow constructs such as 
#  ifs and loops, your solutions can look very different
#  to these sample solutions.
# Make sure that you test your code thoroughly to spot 
#  any hidden bugs!

# Gather name and input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Check the age of the user
if (age < 18):
    # Too young to vote - don't check the nationality as it 
    #  doesn't matter!
    print(f"{name:s} is too young to vote.")
else:
    # If the age of the user is less than 18, then the program
    #  would not reach this else branch. Therefore, the user
    #  must be 18 or over, so we don't need to check again!

    # Get nationality
    nationality = input("Enter your nationality: ")

    # Check nationality
    # Both comparison must be complete. You cannot shortcut as 
    # nationality == "UK" or "Britain" as Python will interpret
    # "Britain" as True - causing the check to be bypassed.
    if nationality == "UK" or nationality == "Britain":
        # Nationality is valid
        print(f"{name:s} may vote.")
    else:
        # Nationality not valid
        print(f"{nationality:s} is not a valid nationality - {name:s} is not eligible to vote.")
    
