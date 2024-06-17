# Get the temperature in farenheit
fahrenheit = float(input("Enter the temperature in Farenheit: "))

# Celsius = (Farenheit -32) * 5/9
celsius = (fahrenheit - 32) * 5/9

# Printing the output
# sep argument defines the characters used to separate the different arguments
# sep = "" means there is nothing extra added between the outputs
#  so it will appear as "71.0f is 21.6666666666668c" when printed out.
print(fahrenheit, " Degrees Fahrenheit is ", celsius, " degrees Celsius", sep = "")

# An alternate way to output a mix of variables and text is the following:
print(f"{fahrenheit:.0f} Degrees Fahrenheit is {celsius:.2f} degrees Celsius")
# This "string format" approach gives you some control over how the values are displayed.
# In this case, using .0f displays a float rounded to the nearest whole number and 
#  .2f displays a float to 2 decimal places.
# String formatting can be a very useful technique to have - give it a practice!
# Useful resource: https://www.w3schools.com/python/ref_string_format.asp