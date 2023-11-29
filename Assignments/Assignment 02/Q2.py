"""
2. Temperature Conversion: (2 Mark)
Write a program that set input in Celsius and converts it to Fahrenheit."""

Celsius= float(input("Value in Celsius :"))
def convert_temperature(Celsius) :
    Fahrenheit=((9/5)*Celsius)+32
    return Fahrenheit

print("Fahrenheit=",convert_temperature(Celsius))

