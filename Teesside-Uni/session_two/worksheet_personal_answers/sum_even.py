# Sum Even Program
# Jordan Picton 10/07/2024

# Declaring the list of values.
integers = [14,5,19,20,21,66,89]

# Declaring a total value at 0.
total = 0

# Initialising a counter with the value of 0.
counter = 0

# While counter is less than the length of the integers list run the code below:
while(counter < len(integers)):
    # If counter is divisible by 2 with no remainder then run the code below:
    if counter % 2 == 0:
        # total is given a new value which is the previous total value plus the value that counter is at within the integers list.
        total = total + integers[counter]
    # Increase counter by 1.
    counter += 1
# Print out the total.
print("The total is:", str(total))