# Diong, Shan Marc C.
# BSCpE 2-2
# September 24, 2024

# Exercise 1: Temperature Converter
# Create a program that converts temperatures between Celsius and Fahrenheit.

#  Word Colors
green = "\033[0;32m"
blue = "\033[0;34m"
yellow = "\033[1;33m"
red = "\033[0;31m"

# Ask the user for input of temperature
print(green + "Welcome to the Temperature Converter!")
temp_value = float(input("Please input the value of the Temperature: "))

# Ask the user to select conversion type from Celsius to Fahrenheit or from Fahrenheit to Celsius
print("\nPlease select a conversion type")
conversion_type = input(f"Type {blue + "'C'" + green} to convert from {blue + "Celsius to Fahrenheit" + green} or type {blue + "'F'" + green} to convert from {blue + "Fahrenheit to Celsius"+ green}: ")

# Conversion and Output result
if conversion_type.upper() == 'C':
    # Celsius to Fahrenheit
    converted_celsius = (temp_value * 9/5) + 32
    print(yellow + f"\n{temp_value}° Celsius is {converted_celsius}° Fahrenheit.")
elif conversion_type.upper() == 'F':
    # Fahrenheit to Celsius
    converted_fahrenheit = (temp_value -32) * 5/9
    print(yellow + f"\n{temp_value}° Fahrenheit is {converted_fahrenheit}° Celsius.")
else:
    # Invalid Input
    print(red + "\nInvalid Input! Please type 'C' or 'F'")

# End