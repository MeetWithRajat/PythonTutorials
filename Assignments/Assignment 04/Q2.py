"""Question 2: Number Guessing Game (5 Marks)
Create a number guessing game. Generate a random number between 1 and 100 and 
ask the user to guess the number. Provide feedback (too high, too low, or correct) 
and allow the user to keep guessing until they correctly identify the number. Use a
 while loop for repeated attempts and include an option to exit the game.
Note: You can take help from internet about random number generation (eg: see link
 given below)."""

import random

number = random.randrange(1,100)
# print(number)

c = 1
while c == 1:
    guess = float(input("Guess the no :"))
    if guess == number:
        print(" Correct .")
        break
    elif number-10 < guess < number+10:
        print("Feedback skill : too high ")
    else:
        print("Feedback skill : too low ") 
    c -= 1
    c = int(input("If you don't want to exit, press 1 :"))

print("Thank you !")