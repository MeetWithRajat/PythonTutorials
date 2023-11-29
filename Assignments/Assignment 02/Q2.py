"""
2. Temperature Conversion: (2 Mark)
Write a program that set input in Celsius and converts it to Fahrenheit."""

Celsius = float(input("Value in Celsius: "))


def convert_temperature():
    fahrenheit = ((9/5)*Celsius)+32
    return fahrenheit


print("Fahrenheit = ", round(convert_temperature(), 1))


# 2.357
#
# 2.35 - string formatting
# 2.36 - round
