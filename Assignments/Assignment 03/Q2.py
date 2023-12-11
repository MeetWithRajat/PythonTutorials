"""format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where
        it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case"""

S2= {'x':"Ankita" , 'y':"Rajat da"}
print("{x} : Hiii {y} !  " .format_map(S2))

print("*****")

S3=['banana', 'apple', 'watermalon']
print(S3.index('watermalon'))

print("*****")

S4="meetwithankita2003"
print(S4.isalnum())
print(S4.isalpha())
print(S4.isascii())
print(S4.islower())

print("*****")

S5="06052003"
print(S5.isdecimal())
print(S5.isdigit())

print("*****")

S6="ankita"
print(S6.isidentifier())