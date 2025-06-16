#A spam comment is defined as a text containing following keywords : "Make a lot of money", "buy now", "Subscribe this", "click this". Write a program to detect this spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "Subscribe this"
p4 = "click this"

message = input("Enter your comment: ")


message_lower = message.lower()

if (p1.lower() in message_lower or 
    p2.lower() in message_lower or 
    p3.lower() in message_lower or 
    p4.lower() in message_lower):
    print("This comment is a spam")
else:
    print("This comment is not a spam")