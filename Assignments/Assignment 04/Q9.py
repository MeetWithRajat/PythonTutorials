"""Question 9: Vowel Counter (3 Marks)
Write a program that takes a sentence as input from the user and counts the 
number of vowels (both uppercase and lowercase) in it. Output the count of each vowel separately"""

line = input("Enter a sentence :")
line2 = line.lower()
key = 0
for i in line2:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        key += 1

if key == 0:
    print("No vowels .") 
else:
    print("Total vowel no :", key)


