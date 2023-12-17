"""isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string"""

S7="Ankita Das"
S8="  "
print(S7.isprintable())
print(S8.isspace())
print(S7.istitle())

print("*****")

S9="123456789"
print(S9.isnumeric())

print("*****")

S10="ANKITA DAS"
print(S10.isupper())
print(S10.lower())
print(S10.ljust(10),"is my name .")
print("My name is", S10.lstrip() ,". I study in 3rd year.")

print("***")

S11=['Ankita', 'Rai', 'Mili']
print("**".join(S11))


print("\n\nCompare")
str1 = "Straße"  # German sharp "ß"
str2 = "strasse"  # English equivalent

# Using casefold()
result_casefold = str1.casefold() == str2.casefold()
print(result_casefold)  # True

# Using lower()
result_lower = str1.lower() == str2.lower()
print(result_lower)  # False
