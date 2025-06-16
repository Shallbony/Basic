
# write a program to find out wheater a student has passed or failed if it requires a totaal of 40 % and least 33% in each ssubjects and take marks as an input from the user

# Input marks for three subjects
marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

# Calculate total percentage
total_percentage = ((marks1 + marks2 + marks3) / 300) * 100

# Check conditions for pass or fail
if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("You passed!")
else:
    print("You failed, try again next year!")
