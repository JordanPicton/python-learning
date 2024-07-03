# Another program with many possible solutions - keep experimenting!

# Gather the input from the user
# Automatically converting the input to lower case to make comparisons
#  easier!
type = input("Enter pokemon type: ").lower()
letter = input("Enter first letter of pokemon name: ").lower()

# Checking type first
if type == "water":
    # Type matches - try to find a matching entry
    if letter == "s":
        print("Pokemon could be Squirtle!")
    elif letter == "t":
        print("Pokemon could be Tentacool!")
    else:
        # No matches with pokemon in this type
        print("No matching Water pokemon.")
elif type == "fire":
    # Type matches - try to find a matching entry
    if letter == "c":
        print("Pokemon could be Charmander!")
    elif letter == "m":
        print("Pokemon could be Moltres!")
    else:
        # No matches with pokemon in this type
        print("No matching Fire pokemon.")
elif type == "grass":
    # Type matches - try to find a matching entry
    if letter == "b":
        print("Pokemon could be Bulbasaur!")
    elif letter == "o":
        print("Pokemon could be Oddish!")
    else:
        # No matches with pokemon in this type
        print("No matching Grass pokemon.")
elif type == "electric":
    # Type matches - try to find a matching entry
    if letter == "p":
        print("Pokemon could be Pikachu!")
    elif letter == "v":
        print("Pokemon could be Voltorb!")
    else:
        # No matches with pokemon in this type
        print("No matching Electric pokemon.")
else:
    # No matches at all
    print("No matches with that type.")
