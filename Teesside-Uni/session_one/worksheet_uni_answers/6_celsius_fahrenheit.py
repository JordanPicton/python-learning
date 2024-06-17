# Get the temperature in farenheit
celsius = float(input("Enter the temperature in Celsius: "))

# Celsius = (Farenheit -32) * 5/9
fahrenheit = (celsius * 9/5) + 32

# Printing the output
# sep argument defines the characters used to separate the different arguments
# sep = "" means there is nothing extra added between the outputs
#  so it will appear as "22 Celsius is 71.6666666666 degrees Fahrenheit." when printed out.
print(celsius, " Celsius is ", fahrenheit, " degrees Fahrenheit.", sep = "")

# An alternate way to output a mix of variables and text is the following:
print(f"{celsius:.0f} Celsius is {fahrenheit:.1f} degrees Fahrenheit.")
# This "string format" approach gives you some control over how the values are displayed.
# In this case, using .0f displays a float rounded to the nearest whole number and 
#  .1f displays a float to 1 decimal place.
# String formatting can be a very useful technique to have - give it a practice!
# Useful resource: https://www.w3schools.com/python/ref_string_format.asp