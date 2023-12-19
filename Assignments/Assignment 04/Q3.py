"""Question 3: Multiplication Table Generator (3 Marks)
Write a program that generates the multiplication table for a given number. 
Take input from the user for the number and use a for loop to print the multiplication table up to 10. 
Allow the user to enter another number or exit the program."""

n = 1
while n == 1:
    number = float(input("Number :"))
    for i in range(11):
        print("{0} * {1} = ".format(i, number), number*i)
    n -= 1
    n = int(input("If you want to generate another multiplication table press 1 :"))
    