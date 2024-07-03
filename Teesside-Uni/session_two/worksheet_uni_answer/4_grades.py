# Simple program to identify the grade based on input marks.

# Get input from the user
# If the user enters something that isn't a number, we will 
#  crash here. There are some things we could do - look into 
#  the "isnumeric()" function or "try" blocks and give it
#  another go!
mark = int(input("Enter the mark: "))

# Checking for invalid mark values
if mark < 0 or mark > 100:
    # Mark not valid
    print("Invalid mark")
# Any valid mark would be less than 100, so we don't need
#  to check the upper limit - we've already made sure its
#  valid.
elif mark >= 70:
    print("Grade A!")
# Since we only reach the next band down if the mark is lower
#  than the upper limit, we just need to check that its above
#  the minimum for a particular grade!
elif mark >= 60:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
elif mark >= 40:
    print("Grade D")
elif mark > 0:
    print("Grade F")
# If the mark is not greater than 0, but still valid, it must
#  be a non-submission, so we can use else.
else:
    print("N/S")