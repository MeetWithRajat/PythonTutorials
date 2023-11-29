"""
1. Type Conversion: (1 Mark)
Write a program that assign two value to two variables as a string and converts it into an 
integer or float, then performs a mathematical operation and displays the result."""

# a = "111"
# b = "222"
a=str(input("Enter any Number :"))
b=str(input("Enter any Number :"))
c = float(a)
d = int(b) 
print(a,type(a))
print(b,type(b))
print(c,type(c)) 
print(d,type(d))

# result = c*d
# print(result)

print("Menu::\n1 for ADDITION\n2 for SUBTRACTION\n3 for MULTIPLICATION\n4 FOR DIVISION\n5 for REMAINDER OF DIVISION")
choice=int(input("Enter the choice between 1 to 5 :"))
if(choice==1):
    result=c+d
elif(choice==2):
    result=c-d
elif(choice==3):
    result=c*d
elif(choice==4):
    result=c/d        
elif(choice==5):
    result=c%d
else:
    print("Incorrect choice .")       

print("Result ::",result)     