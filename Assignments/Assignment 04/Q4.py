"""Question 4: Password Checker (5 Marks)
Implement a simple password checker. Ask the user to enter a password, and check if 
it meets certain criteria (e.g., minimum length, presence of numbers and special characters).
 Provide appropriate feedback using if-else statements. Use a while loop to keep prompting
 the user until they enter a valid password."""

password = input("Enter the password :")

while True:
    if len(password) < 8:
        print("Password must be at least 8 characters.")
        break
    if not any(i.isdigit() for i in password):
        print("Password must contain at least one digit.")
        break
    if not any(i in r"!@#$%^&*()-_+=[]{}|;:'\",.<>/?`~" for i in password):
        print("Password must contain at least one special character.")
        break
    print("Password is valid!")
    break
