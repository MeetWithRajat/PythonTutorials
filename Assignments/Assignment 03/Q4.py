"""
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
"""
S1="Ankita Das"
print(S1.translate(S1.maketrans("D","S")))

S2="My name is ANKITA DAS .I study in 3rd year"
print(S2.partition("DAS"))
print(S2.replace("DAS","SASMAL"))

S3= "I am a girl. I am a student ."
print(S3.rfind("I"))
print(S3.rindex("I"))
print(S3.rjust(20))
print(S3.rpartition("I"))
print(S3.rsplit("I"))

S10="ANKITA DAS"
print("My name is", S10.rstrip() ,". I study in 3rd year.")