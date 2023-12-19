"""Question 6: Prime Number Checker (7 Marks)
i. Create a program that checks if a given number is prime. ----> (4 Marks)
ii. Create a program that checks if a given year is leap year. ----> (3 Marks)"""

no = int(input("Check the Number is prime or not:"))

if no < 2:
    print("1 is a non-prime no .")
else:
    key = 0
    r = no*0.5
    for i in range(2, int(r+1)):
        if no % i == 0:
            key += 1

    if key == 0:
        print("{0} is prime no .".format(no))
    else:
        print("{0} is non-prime no .".format(no))    


print("*******************************")        

year = int(input("Enter a year :"))

if (year % 4 == 0) & (year % 400 == 0):
    print("Year is leap-year .")
elif (year % 4 == 0) & (year % 100 != 0):
    print("Year is leap-year .") 
else:
    print("Year is not leap-year.")    

