"""Question 1: Simple Calculator (3 Marks)
Write a program that acts as a simple calculator. It should take input for two numbers and an operator (+, -, *, /). Use if-else statements to perform the corresponding operation and output the result. Implement a loop that allows the user to perform multiple calculations
until they choose to exit."""

n = int(input("If you want to calculate press 1 :"))
while n == 1:
    no1 = float(input("First digit :"))
    no2 = float(input("Second digit :"))

    print("1 for ADDITION\n2 for SUBTRACTION\n3 for MULTIPLICATION\n4 for DIVISION")
    option = int(input("Choice :"))
    if option == 1:
        print("{0}+{1}=".format(no1, no2), no1+no2)
    elif option == 2:
        print("{0}-{1}=".format(no1, no2), no1-no2)
    elif option == 3:
        print("{0}*{1}=".format(no1, no2), no1*no2)
    elif option == 4:
        print("{0}/{1}=".format(no1, no2), no1/no2)
    else:
        print("Incorrect option !!")   

    n = 0
    n = int(input("If you do not want to exit press 1 otherwise any digit :"))
    if n != 1:
        print("Thank you !")    
        break 
