# Simple Comparison Program
# Jordan Picton 03/07/2024

# Delcaring variables.
firstName = input("Please insert your first name: ") # Input variable asking user for firstname.
lastName = input("Please insert your last name: ") # Input variable asking user for lastname.
fullName = firstName + " " + lastName # Variable storing the combined input of the users name.
userAge = int(input("Please insert your age: ")) # Input variable asking user for age.
userCitizenship = input("Please enter your citizenship country: ") # Input variable asking user for citizenship.

# Main IF statement.
if userAge < 18: # Checks to see if the user is under 18.
    print(fullName, ". You are not old enough to vote. You must be 18 or over.") # Prints out a message informing they're ineligible for voting.
elif userCitizenship.upper() == "UK" or userCitizenship.upper() == "BRITAIN": # Check to see if the user is UK or British.
    print(fullName, ". You are eligible to vote.") # Prints out a message informing the user is eligible for voting.
else: # Anything else, run the code below.
    print(fullName, ". You are of the correct age, but you don't have the correct citizenship. Meaning you're not eligible to vote.") # Prints out a message informing they're ineligible for voting.