
a = "Ankita"
b = a
del a
print(b)
# print(a) # this will give error because a is deleted (delete the link not actual value because b is using it)

x = [1, 2, 3]
y = x
y[0] = 5
del x

print(y)
