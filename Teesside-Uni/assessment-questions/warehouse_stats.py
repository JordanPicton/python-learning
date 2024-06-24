# Warehouse Weight Statistics
# Jordan Picton - 24/06/2024

# Importing Libraries.
import statistics

# Defining variables.
deliveries = [] # Assiging deliveries as an empty array.
loop = 0 # Assings loop as 0 to be used in a loop later.

# Main Program.
deliveryNum = int(input(("Please enter the amount of deliveries you would like to input (Must be 10 or more): "))) # Asks the user for the amount of deliveries they are inputting. (Casts the input to an Integer)
# While loop to ensure the number of deliveries is going to be 10 or more. If it is lower than 10 then the user will be asked to input at elast a value of 10 or more.
while deliveryNum < 10:
  deliveryNum = int(input(("Sorry please try again, enter the amount of deliveries you would like to input (Must be 10 or more): "))) # (Casts the input to an Integer value)

deliveries.append(float(input("Please insert your deliveries weight: "))) # Adds the user input to the deliveries empty array. (Casts the input to a Float value)

# Loops through the code until loop is no longer less than deliveryNum.
# Meaning that the user can input new values for each delivery to a new position within the array/list.
while loop < deliveryNum - 1: # Because the array starts at 0 I need to negate 1 value from the delivery num.
  deliveries.append(float(input("Please insert your next deliveries weight: "))) # Add a new value to the deliveries array. (Casts the input to a Float value)
  loop = loop + 1 # Adds one value to the loop variable. (Increment)
  #print(deliveries) # Gives a nice print out of the deliveries array, mainly used for testing.

average = str(statistics.fmean(deliveries)) # Stores the average value of the deliveries array/list. (Casts the input to a String value)
#print(average) # Prints out the average value, mainly used for testing.
median = str(statistics.median(deliveries)) # Stores the madian value of the deliveries array/list. (Casts the input to a String value)
#print(median) # Prints out the median value, mainly used for testing.
maximum = str(max(deliveries)) # Stores the maximum value of the deliveries array/list. (Casts the input to a String value)
#print(maximum) # Prints out the max value, mainly used for testing.
minimum = str(min(deliveries)) # Stores the minimum value of the deliveries array/list. (Casts the input to a String value)
#print(minimum) # Prints out the min value, mainly used for testing.

# Print out for the different arithemtic values for the deliveries array/list. Casts deliveryNum to a String data type to allow for it to be used with the + symbol (Concatenation).
# Also I've used the "\n" special character to shift the different values to the next line, whilst also setting the default separator to be nothing, not even white space.
print("Delivery Statistics\n", "------------------\n", "Deliveries: ", str(deliveryNum) + "\n", "Average Weight: ", average + "\n", "Highest Weight: ", maximum + "\n", "Lowest Weight: ", minimum + "\n", "Median Weight: ", median + "\n", "------------------", sep="")