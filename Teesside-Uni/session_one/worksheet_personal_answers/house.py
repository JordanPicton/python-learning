# Room 1 Input
roomOneLength = int(input("Please enter the length of room 1: ")) # Input for Length.
roomOneWidth = int(input("Please enter the width of room 1: ")) # Input for Width.
roomOneHeight = int(input("Please enter the height of room 1: ")) # Input for Height.
print("")
# Room 1 Input
roomTwoLength = int(input("Please enter the length of room 2: ")) # Input for Length.
roomTwoWidth = int(input("Please enter the width of room 2: ")) # Input for Width.
roomTwoHeight = int(input("Please enter the height of room 2: ")) # Input for Height.
print("")
# Room 1 Input
roomThreeLength = int(input("Please enter the length of room 3: ")) # Input for Length.
roomThreeWidth = int(input("Please enter the width of room 3: ")) # Input for Width.
roomThreeHeight = int(input("Please enter the height of room 3: ")) # Input for Height.
print("")
# Room 1 Input
roomFourLength = int(input("Please enter the length of room 4: ")) # Input for Length.
roomFourWidth = int(input("Please enter the width of room 4: ")) # Input for Width.
roomFourHeight = int(input("Please enter the height of room 4: ")) # Input for Height.
print("")

# Room One Calculations
roomOneArea = roomOneWidth * roomOneLength
roomOneVolume = roomOneArea * roomOneHeight

# Room Two Calculations
roomTwoArea = roomTwoWidth * roomTwoLength
roomTwoVolume = roomTwoArea * roomTwoHeight

# Room Three Calculations
roomThreeArea = roomThreeWidth * roomThreeLength
roomThreeVolume = roomThreeArea * roomThreeHeight

# Room Four Calculations
roomFourArea = roomFourWidth * roomFourLength
roomFourVolume = roomFourArea * roomFourHeight

# Total Calculations
areaTotal = roomOneArea + roomTwoArea + roomThreeArea + roomFourArea
volumeTotal = roomOneVolume + roomTwoVolume + roomThreeVolume + roomFourVolume

# Outputs
print("Square footage total is", areaTotal, "square feet.\nVolume total is", volumeTotal, "cubic feet.")