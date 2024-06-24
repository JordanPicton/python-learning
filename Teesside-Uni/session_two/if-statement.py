# Collecting inputs from user.
inputOne = int(input("Enter a number: "))
inputTwo = int(input("Enter another number: "))

# Main Program
if inputOne > inputTwo:
  print(inputOne, "is the biggest!")
elif inputTwo > inputOne:
  print(inputTwo, "is the biggest!")
else:
  print("Both are equal!")