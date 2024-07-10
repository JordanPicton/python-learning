# Sum Even Program
# Jordan Picton 10/07/2024

# Declaring the list of values.
integers = [14,5,19,20,21,66,89]

# Declaring a total value at 0.
total = 0

# Initialising a counter with the value of 0.
counter = 0

while(counter < len(integers)):
    if counter % 2 == 0:
        total = total + integers[counter]