# Pokemon Program
# Jordan Picton 04/07/2024

print("The types of pokemen accepted are shown below.")
print("A - Fire")
print("B - Water")
print("C - Grass")
print("D - Electric")
print("You only need to use A, B, C or D!")

elementType = input("Enter the Pokemon Type: ").lower()
pokemonLetter = input("Enter the first letter of the pokemon: ").lower()

if elementType == "b":
    if pokemonLetter == "s":
        print("The Pokemon could be Squirtle!")
    elif pokemonLetter == "t":
        print("The Pokemon could be Tentacool!")
    else:
        print("Sorry there is no matching water Pokemon within our database.")
elif elementType == "a":
    if pokemonLetter == "c":
        print("The Pokemon could be Charmander!")
    elif pokemonLetter == "m":
        print("The Pokemon could be Moltres!")
    else:
        print("Sorry there is no matching fire Pokemon within our database.")
elif elementType == "b":
    if pokemonLetter == "b":
        print("The Pokemon could be Bulbasaur!")
    elif pokemonLetter == "o":
        print("The Pokemon could be Oddish!")
    else:
        print("Sorry there is no matching grass Pokemon within our database.")
elif elementType == "c":
    if pokemonLetter == "p":
        print("The Pokemon could be Pikachu!")
    elif pokemonLetter == "v":
        print("The Pokemon could be Voltorb!")
    else:
        print("Sorry there is no matching electric Pokemon within our database.")
else:
    print("No matches with that type.")