"""
Question 8: Reverse The Number (3 Marks)
Write a program that take input from user,
convert it to integer and then reverse the digits of the number and print."""

number = input("Any number :")

no = int(number)
no1 = 0
while no != 0:
    r = no % 10
    no1 = no1*10 + r
    no = no // 10
print(no1)


    