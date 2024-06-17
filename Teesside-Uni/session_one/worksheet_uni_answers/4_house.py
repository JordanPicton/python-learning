# This solution is not the most efficient way to approach the problem.
# We will cover better approaches and techniques as the module progresses.
# Why not come back to this one later on?

# Input and calculations for room 1
room1_length = int(input("Enter the length of room 1: ")) # Get the length
room1_width = int(input("Enter the width of room 1: ")) # Get the width
room1_height = int(input("Enter the height of room 1: ")) # Get the height
room1_area = room1_width * room1_length # Caluclate the area of room 1
room1_volume = room1_area * room1_height # Calculate the volume of room 1
print()

# Repeat the code for room 2
room2_length = int(input("Enter the length of room 2: "))
room2_width = int(input("Enter the width of room 2: "))
room2_height = int(input("Enter the height of room 2: "))
room2_area = room2_width * room2_length
room2_volume = room2_area * room2_height
print() # Extra space in the shell to make reading the output easier

# Repeat the code for room 3
room3_length = int(input("Enter the length of room 3: "))
room3_width = int(input("Enter the width of room 3: "))
room3_height = int(input("Enter the height of room 3: "))
room3_area = room3_width * room3_length
room3_volume = room3_area * room3_height
print()

# Repeat the code a final time for room 4
room4_length = int(input("Enter the length of room 4: "))
room4_width = int(input("Enter the width of room 4: "))
room4_height = int(input("Enter the height of room 4: "))
room4_area = room4_width * room4_length
room4_volume = room4_area * room4_height
print()

# Calculate the totals
total_area = room1_area + room2_area + room3_area + room4_area
total_volume = room1_volume + room2_volume + room3_volume + room4_volume

# Print out the results
print("The total square footage is", total_area, "square feet.")
print("The total volume is", total_volume, "cubic feet.")