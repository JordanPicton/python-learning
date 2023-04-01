# Below shows two ways on how to get a new line within Python
print("The itsy bitsy spider climbed up the waterspout.")
# The print statement below doesn't have any arguments meaning it will be empty. But there will be something that gets printed. It won't just entirely be blank.
# What happens when this is used is that there is an empty line that will be printed in the console with no actual content just a completely blank line.
print()
print("Down came the rain and washed the spider out.")

# Where as using the example below I can have a single print statement without needing to fill the source file with a bunch of print statements, I can use the 
print("Out came the sun, and dried up all the rain\nand the itsy bitsy spider went up the spout again")

# If I want to display a backslash I and not use an escaping part of it I would need to double the backslash to make sure it doesn't mess something up like combining with other characters such as n and t. (n = newline, t = tab. There are more though.)
print("Hello this is a \\test")

# Below shows the use of using different arguements withing the print statement. This has three Strings for the arguments and is pretty similar to how Java would print out something to console.
print("String 1","String 2","String 3")

# With the example below there is no space at the beginning of the string. The number 82 also doesn't have/give a space. However when ran and read inside the console the String data type takes the initiative and places a space when there is another 
# arguement before or after meaning if there is an arguement after the String on the same print invocation then it will automatically put a space at the end of the String itself to separate the two arguements.
print(82,"test")

# Signature
print("Author: Jordan Picton  -  Date: 01/04/2023")