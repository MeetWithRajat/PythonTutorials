"""
4. Email Template: (1 Mark)
Create a simple email template with placeholders for the recipient's name and a generic message. 
Use string formatting to personalize the email for different recipients.
"""
recipient = input("Recipient Name: ")
gmail_recipient = input("Recipient Email-id: ")
subject = input("Subject of this Email: ")
generic_msg = input("Enter your generic message: ")
messenger = input("Person name,who deliver the message: ")
gmail_messenger = input("Email id of messenger: ")

print("\nTo {0}".format(gmail_recipient))
print("Subject : {0}\n".format(subject))
print("Dear {0},".format(recipient))
print("          {0}".format(generic_msg))
print("\nBest regards,\n{0}\n{1}".format(messenger, gmail_messenger))
