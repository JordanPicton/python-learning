#Within this program I'll be playing around with the print function after learning about it a little more.
#1. The task at hand is to get the code below to output the following: Programming***Essentials***in...Python
print("Programming", "Essentials", "in",sep="***",end="...")
print("Python")

#2. The task below asks me to turn the below commented out arrow to use less print invocations. Then make it twice as large. I then have to duplicate the arrow and have them be printed side by side. Removing a quotation mark from one of the strings
#below, allows me to see that the error message doesn't exactly tell me where within the invocation the error is located. But more or less a general area within where the code itself finds it.
# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")
print("    *     "*2, "   * *    "*2, "  *   *   "*2, " *     *  "*2, "***   *** "*2,
      "  *   *   "*2, "  *   *   "*2, "  *   *   "*2, "  *   *   "*2, "  *****   "*2, sep="\n")

#Something new to learn is a new data type which comes with new issues it's the literal data type. Literals are basically the integers almost of python it seems.
#"123" is a literal but "c" is not. As you can see from the examples below there is an output with quotation marks and then an output without these quotation marks, and if we were making Strings then we would expect the second output to error.
#However since I'm using a number for these example it will not error due to a number without quotation marks in this case is a literal. Where as if I tried this with a word or any other character that was not a number it would through an error.
#Python knows that by using a number here it's a literal.
print("2")
print(2)

#Within Python I can write literals with underscores to make them easier to read. I can't write them like this: 123,456,789 or 123.456.789 or even 123 456 789. To get the same thing but that is actually allowed within Python I would need to write it
#in the similar fashion as the one below.
print(123_456_789)
#Wiritng negative numbers is done like this "-123_456789" and I don't need to use a plus sign for the positive number but Python does allow it. Meaning "123456789" is the same as "+123456789".

#There are also octal and hexadecimal numbers I can look into, these work differently to normal numbers. If a number has the prefix of "0O" or "0o" then it would be treated as an octal value, however when doing this the numbers can only go up to 7.
#For example if I had an octal number such as "0o472" then this would work, however "0o728" would not due to the 8 being higher than the number 7.
#0o123 is an octal number with a decimal value equal to 83.
print("I am an octal",0o723) #I just confrirmed this by setting the test number here to being "0o728" and getting an error about an invalid digit within an octal literal. (0-7)

#The second convention is called hexadecimal and it's very similar to how the octal convention works. Instead of using "0o" or "0O" as it's prefix, hexadecimal uses "0X" or "0x" as the prefix.
#The hexadecimal value of "0x123" is the equivalent of the decimal value "291"
print("I am a hexideciaml",0x923) #With hexadecimals it seems I can use numbers above 7. (0-9)

#Floats are next literal and well I remember these from Java so they shouldn't be too hard to figure out. Basically it's a number that allows for fractions of a decimal number. Meaning there can be a full decimal number or some of a decimal number
#after the decimal number point. Normally a number like "0.4" would be written like I've just done it however, if there is no number infront of the decimal point then I can omit the 0. Meaning it can look like ".4" instead of "0.4".
#This works in the other direction, for example "4.0" can be shortened down to "4."
print("I am a float =",0.82)

#Moving onto some more things about ints and floats. So normally when reading the numbers "4" and "4.0" respectively, we would belive them to be the same if thinking about Math. However when Python reads this it will read the "4" as an integer and the
#"4.0" as a float. They have different meaning and store different values. The decimal point is not the only thing that makes a number to a float. You can also use the letter "e". Using the letter is a short hand for very large or small numbers.
# This is similar to what we do in Math too. For example the speed of light is expressed in MPS(Meters per second) and written directly would look like the following: 300000000. Within Math questions there are easier ways to show this like for example,
#3 x 10^8 is the same as what I wrote earlier, it just means 3 times 10 to the power of 8 (it has eight zeros.).
print("This is an easier way to print numbers like =", 3e8)
#The example above allows me to print the number out in an easier way than writing out all the other 0's.
#Somethings to note are; the exponent (the value after the E) has to be an integer. And the base (the value in front of the E) may be an integer.