# This example is one where a "simple" solution is to code the
#  additions directly - values[0] + values[2] + ...
# But we don't want our programs to be so fixed - we want to
#  write solutions that will work for any list!

# Creates the list with the specified values
values = [14,5,19,20,21,66,89]

# Will show two approaches to solving this problem: a while 
#  loop and a for loop
# Both valid!

# Set up counter outside the loop - we want to use the same
#  value for all of the iterations!
total_while = 0

# We also set up a counter to act as our index tracker
count = 0

# The while loop will run as long as count (the index) will
#  point to a valid location in the list
while(count < len(values)):
    # Check that the index is an even index
    if count % 2 == 0:
        # even index; load the value from the list at the 
        #  even index and add it to the total
        total_while = total_while + values[count]
    
    # Increase the counter by one - will need to do this 
    #  whether it is currently even or odd, so outside the if
    count += 1

print(f"Total is {total_while:d}")

# This alternate approach will use a for loop.
# This loop will try every value in a particular collection, running
#  the loop body once. This value will also be available inside the 
#  loop via the loop counter - i in this case.

# We create a new total, so we can compare the two approaches!
total_for = 0

# We create our for loop - this loop will run until every value in the
#  specified range is checked.
# In this example, the range will start at 0, end when the range hits the 
#  length of the list and go up by 2 each time
for i in range(0, len(values), 2):
    # Since the loop counter starts at 0 - an even number - and goes up by 2
    #  each time, ONLY even indicies will be considered!
    # No further checks needed!
    total_for = total_for + values[i]

print(f"Total is {total_for:d}")