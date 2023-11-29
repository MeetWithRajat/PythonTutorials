"""
3. BMI Calculator: (2 Mark)
 Write a program that calculates the Body Mass Index (BMI) using static input for weight (in kilograms) 
 and height (in meters). Display the BMI as a float."""

height = float(input("Height of person in Meter: "))
weight = float(input("Weight of person in kilogram: "))
BMI = weight/height**2

print(type(BMI))
print("BMI of this person: ", BMI)
