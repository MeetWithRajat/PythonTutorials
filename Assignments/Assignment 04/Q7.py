"""Question 7: Fibonacci Sequence Generator (3 Marks)
Implement a program that generates the Fibonacci sequence up to a specified term.
Take input from the user for the number of terms they want to 
generate and use a for loop to calculate and print the Fibonacci sequence."""

no = int(input("Enter the highest range :"))

sum = 0
a = 0
b = 1
print("0\n1")                 
for i in range(no):
   if sum < no:
    sum = a + b
    print(sum)
    a = b
    b = sum




