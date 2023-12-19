"""Question 5: Factorial Calculator (3 Marks)
Write a program that calculates the factorial of a given number. Take input from the
 user and use a for loop to calculate the factorial. Handle the case where the input is not a 
positive integer by providing an appropriate error message."""

facto = int(input("Give a number :"))
mul = 1

if facto < 0:
    print("Factorial function is not defined for negative integer .")
elif facto == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, facto+1):
        mul *= i
        i += 1
    print("Factorial of {0} is {1}".format(facto, mul))


