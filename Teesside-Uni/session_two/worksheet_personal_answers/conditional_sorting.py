# Conditional Sorting Program
# Jordan Picton 03/07/2024

# Declare variables. (User inputs)
# numOne = int(input("Please insert your first number: ")) # Takes user input to give the variable a value.
# numTwo = int(input("Please insert your second number: ")) # Takes user input to give the variable a value.
# numThree = int(input("Please insert your third number: ")) # Takes user input to give the variable a value.

flag = True

# Nested IF Program.
while flag:

    # Takes user input to give the variable a value.
    numTwoIF = input(
        "Please insert your second number or 'exit' to quit the program: ")

    if numOneIF == "quit" or numTwoIF == "quit":
        flag = False
    else:
        # Takes user input to give the variable a value.
        numThreeIF = input(
            "Please insert your third number or 'exit' to quit the program: ")

        if numThreeIF == "quit":
            flag = False
        else:
            numOneIF = int(numOneIF)
            numTwoIF = int(numTwoIF)
            numThreeIF = int(numThreeIF)

            # Comparing the Numbers
            if numOneIF > numTwoIF:
                if numOneIF > numThreeIF:
                    print("Wrong1")
                else:
                    print("Wrong2")
            else:
                print("Wrong3")


# List Program.

    # Declare variables
    numList = []
    numOneList = input(
        "Please insert your first number or 'exit' to quit the program: ")
    numOneList = input(
        "Please insert your second number or 'exit' to quit the program: ")
    numOneList = input(
        "Please insert your third number or 'exit' to quit the program: ")

    while flag:
        # Takes user input to give the variable a value.
        numOneList = input(
            "Please insert your first number or 'exit' to quit the program: ")
        if numOneList == "quit":
            flag = False
        else:
            numList.append(int(numOneList))  # Adds the value from
        print(numList)
