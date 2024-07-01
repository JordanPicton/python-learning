# Declaring a list
# Declares a list with integer values.
listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0  # Sets a counter variable.

# len us a function that gives me the length of the list. In this case listOne.
# So the counter is declared as 0, so while counter is lower than the list, then it will countinue to loop until it's not.
# With every iteration of the code block the counter is incremented.
while counter < len(listOne):
    print("Value:", counter)
    counter += 1


################### Some other examples shown off below ####################

#### List Example One (Games)
# Delcaring a new list with String values.
games = ["Terraria", "Minecraft", "Call of Duty",
         "Elder Scrolls V: Skyrim", "Stellaris"]
# Printing out the value of the games list.
print("The games list contains the values of:", games)

# Collection of the 3rd game within the games list.
# This is a 2 becuse the list starts at 0 indexing and not 1, similar to other languages.
gameThree = games[2]
# Printing out the value of the gameThree.
print("The third game within the games list is as follows:", gameThree)
print("The value within the 3rd item of the games list is equal to the value of Call of Duty, True/False?",
      games[2] == "Call of Duty")  # This should print out true.

#### List Example Two (Multipliers)
multipliers = [100, 200, 3, 17] # Declaring a new list.
counter = 0 # Declaring counter variable with value of 0.

# While loop, loops through until the counter is no longer below the value of the length of the multipliers list.
print("While Loop Example:")
while counter < len(multipliers):
    # Prints out the value of the multipliers postion with the help of the counter value to select the item within the multipliers list.
    # Then prints out the String of "times 5 equals".
    # Then mulitplies the value of the counters position within the multipliers list by 5.
    print(multipliers[counter], "times 5 equals", multipliers[counter] * 5) # Print multiplier * 5.
    # Increments counter by 1 so the program doesn't cause an infinite loop.
    counter += 1 # Without this, the program will enter a inifinite loop where the output will continously be 100 times 5 is 500.
    #counter = counter + 1 # Same semantics as line above.

# For loop, when it comes to the for statement it is specialised for these lists. You can't use for unless there is a list.
# Lists and for statements go hand in hand. Using this method, it allows for a cleaner iteration/looping over lists.
print("For Loop Example:")

multipliersTwo = [33, 72, 88, 22] # Declaring a new list.
# With the for loop there is no need to add a counter variable as it handles this for me right off the bat.
# The example for loop below does the exact same thing that the while loop above does. Instead of counter I've used num here to display that basically.
# This is a more reliable way to write loops as it is impossible to create an infinite for loop.
for num in multipliersTwo:
    print(num, "times 5 equals", num * 5) # Print multiplier * 5.