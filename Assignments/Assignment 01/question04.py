# Question no 4 ::Swap the values of two variables, a and b, and print the updated values.
a = 2
b = 3

a = a+b
b = a-b
a = a-b

print("Updated value of a and b is respectively :: ", a, b)

# Pythonic way
x = "abcd"
y = 6
x, y = y, x
print("Updated value of x and y is respectively :: ", x, y)
