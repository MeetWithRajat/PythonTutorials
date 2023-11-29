# https://www.w3schools.com/python/python_operators.asp

x = 5

if x == 5:
    print("x equals to 5")

if x is 5:
    print("x is 5")     # warning

my_list1 = [1, 2, 3]
my_list2 = [1, 2, 3]

if my_list1 == my_list2:
    print("==")

if my_list1 is my_list2:
    print("is")

if x is True:   # Conversion - > "is" should be used for predefine keyword instead of "=="
    print("==")
else:
    print("not")

if 3 in my_list1:
    print("Yes present")
else:
    print("Not present")


a = 5       # 101
b = 3       #  11

print(a & b)    # 001 -> 1
print(a | b)    # 111 -> 7
print(~a)
