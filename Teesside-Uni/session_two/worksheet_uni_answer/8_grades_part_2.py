# This example assumes you are already familiar with the grades solution from Q4
# This version will take a students name and mark and store a set of outputs in a list
#  to be printed out at the end of the program.

grades = []

# Create a flag to let us end the loop when the user is finished.
quit = False

# Start a loop to allow us to keep adding grades indefinitely
while quit == False:
    name = input("Etner the student name [exit to finish]: ")

    # Check if the user wants to quit
    if name == "exit":
        # User does want to quit - set the flag to True
        #  so the loop will end
        quit = True
    else:
        # User has entered a name
        mark = int(input("Enter the students mark [0 - 100]: "))

        # Slightly modified grading solution from Q4
        # Confirm the mark is valid
        if mark < 0 or mark > 100:
            # Mark not valid - program does nothing and goes back to
            #  the start of the loop
            print("Invalid mark - try again.")
        elif mark >= 80:
            # Mark valid - create an output string and add it to the list
            # Must convert mark to a string to combine it in this way
            grades.append(name + " A* (" + str(mark) + ")")
        elif mark >= 70:
            # Same operation for the rest of the valid grades
            grades.append(name + " A (" + str(mark) + ")")
        elif mark >= 60:
            grades.append(name + " B (" + str(mark) + ")")
        elif mark >= 50:
            grades.append(name + " C (" + str(mark) + ")")
        elif mark >= 40:
            grades.append(name + " D (" + str(mark) + ")")
        elif mark > 0:
            grades.append(name + " F (" + str(mark) + ")")
        else:
            grades.append(name + "N/S (" + str(mark) + ")")

# Loop has ended: output all the entered data
# Another version of the for loop - loads the values from a collection
#  directly. Great for using all values in a list.
# This loop will print all items in the grades list.
for s in grades:
    print(s)