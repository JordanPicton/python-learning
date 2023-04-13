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

# Something I just found out and is very cool is that to define a variable it's done very simply by the example below:
# Variable name=variabletype/value
fname = "Jordan"
# As you can see above, fname is the variable name and then Jordan is the value. This is a String Variable, I'm assuming it knows this because I have parenthesis. Below I will print the fname variable to console.
print(fname)

# The actual way I was supposed to use the variable above, which is apparently called Keyword Arguement in this regard because it's a keyword given to a value and we're using that keyword instead of the actual value itself. It's just easier
# to use a keyword over remembering a value. But I would remember them as variables really since I learned some very basic Java first and that's what I learned from there. However, below is what I was actually supposed to learn.
print("This is just a","test.",end=" ")
print("This 'should' be on a new line.")
# As you can see from the example above it's similar to the examples from line 14 and 21 combined almost. However this isn't the only thing it does. There are two print invocations above, meaning when the first one ends the second will be
# executed after and will be on another line. Though there is a way to manipulate this, as from the example above the word "end" is where the actual keyword arguement comes from and I was getting it mixed up with thinking it was a variable. 
# (I was rushing to the conclusion.) But how this actually works is by changing the way the print statement works. Normally the print statement after closing will go to the next line due to the program running through the arguments for the first
# print statement but the way to manipulate this is by doing the example above, call end which is an Keyword Argument. When calling this and giving it the value of " ", it will not start on a new line and continue the next print on the same line.
# In other cases it might not be a print statement so I'm not sure how it would work in those cases. The default value of the end Keyword Argument is as follows: end="\n".
# Another way of doing this is shown below - The difference being there is no space between the quotation marks: 
# print("This is just a", "test.", end="")
# print("This 'should' be on a new line.")

#This isn't the only behaviour of the print() function I can manipulate however, if I remember above with the example on line 15 then I will know that I can print out multiple Strings within one print fucntion. When doing this it separates them with a
#space by default, but what if I wanted to change that behaviour? Then I would have to edit the "sep" argument, similar to the end argument the sep argument stands for separation (I'm assuming at least) and I can change the way the separation between
#the Strings or other arguments within the print function combine together. An example of this is shown below, I first give it a couple of Strings and then edit the sep argument to make it act differently.
#With the example below if I just put "-" then it will join the lines with a hyphen and only a hyphen meaning it would look like this "Hello my name is Jordan-I am an aspiring developer." So it does work the way I expected. I just changed it to
#also include some spaces, just to make it look nicer when printed in console. (The sep arguments can also be left empty like end. Just removes the space entirely.)
print("Hello my name is Jordan","I am an apsiring developer.",sep=" - ")

#In the little snippet of code below is me just messing around with both keyword arguments in one invocation. I've been given the examples from Python Institute and will be messing around with them and noting down what I find. Okay I will now try
#explaining this to the best of my knowledge because at first I didn't understand but after reading it a little closer it makes sense. I just assumed and then I caught on.
print("My", "name", "is", sep="_", end="*") #This replaces the separations with underscores(_) and then at the end it will have the star(*) character. Not only that but since the default value of the end keyword argument has been overidden it won't go
#to the next line, it will just continue on the same line and end with a star character(*).
print("Monty", "Python.", sep="*", end="*\n") #With this line, it would continue on from the previous line and have all of it's separations show a star(*) character instead of a space. Along with having a star(*) character at the end of the of the printed
#line along with also going to the next line, meaning the next output (if any) is on the next line.

# Signature
print("Author: Jordan Picton  -  Date: 01/04/2023")