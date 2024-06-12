# Takes one input from the user and stores it in the variable x.
x = input("Please insert a number: ")
# Takes a second input from the user and stores it in the variable y.
y = input("Please insert another number: ")

# Below casts the variable X's and Y's value as a number as when the user inputs their values they're classed as Strings.
x = int(x)
y = int(y)

# Prints out a String message along with the combination of x+y.
print("Your first and second input added together comes to the total of:",x+y)