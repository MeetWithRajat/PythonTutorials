"""
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

S1="Hii ! I am Ankita ."
print(S1.split("am"))

S2="I love Rabindra-sanget \nand\n Bankim Chandra Chattopadhyay."
print(S2.splitlines())
print(S2.startswith("I"))

S3=" and "
print("Rabindra",S3.strip(),"Najrul")

S4="RABINDRA and najrul."
print(S4.swapcase())

S5="my name is ankita das."
print(S5.title())
print(S5.translate({97:65}))   # 97=a and 65=A (ascii value )
print(S5.upper())

S6="50"
print(S6.zfill(6))