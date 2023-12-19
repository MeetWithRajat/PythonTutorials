"""
Question 10: Prime Factorization (5 Marks)
Implement a program that takes an integer input from the user and prints 
its prime factorization. For example, if the input is 12, the output should be
 2 * 2 * 3. Handle invalid inputs gracefully."""


number = int(input("Enter a number :"))

factors = []
div = 2
while number > 1:
    if number % div == 0:
        factors.append(div) 
        # print(div)
        number = number // div
    else:
        div += 1
        
print("Prime factors are :",  "*".join(map(str, factors)))
    

