"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""

a = 3
b = 4.5
c = "rajat"

print(type(a), type(b), type(c))
print(type(print))
print(type(print()))
print(type(type))

x = float(a)
print("value", x, "Type", type(x))

y = int(b)
print("value", y, "Type", type(y))

# Boolean
b = True
c = False

print(b)
