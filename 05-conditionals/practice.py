#Ask the user for a number. Print "Positive", "Negative", or "Zero".
user_number = int(input("Enter your number: "))
if user_number > 0:
    print("Positive")
elif user_number < 0:
    print("Negative")
else:
    print("Zero")

#Ask the user for an integer. Use % to print whether it's even or odd
integer = int(input("Enter the number: "))
if integer % 2 == 0:
    print("Even")
else:
    print("Odd")
#Ask for the user's age. Print "Invalid age" if it's below 0,
#"Child" if it's below 13, "Teenager" if it's below 18, and "Adult" otherwise.
user_age = int(input("Enter your age: "))
if user_age <= 0:
    print("invalid Age")
elif user_age <= 13:
    print("Child")
elif user_age <= 18:
    print("Teenager")
else:
    print("Adult")

#Store a correct username = "admin" and password = "1234" in variables. Ask the user for both. Print "Welcome" if both match.
#If only the username is right, print "Wrong password". Otherwise print "Unknown user". Use a nested if for this one.
user_name = input("Enter your username: ").strip()
password = int(input("Enter your password: "))

if user_name == "admin":
    if password == 1234:
        print("Welcome")
    elif password != 1234:
        print("Wrong Password")
else:
    print(type(password))
    print("Uknown User")

#Mini program with match/case: Ask the user for a day number from 1 to 7. Use match/case to print the day name (1 is Monday).
# Use case 6 | 7: to print "Weekend" for Saturday and Sunday, and case _: to print "Invalid day" for everything else

day = int(input("Enter your day's number(from 1 to 7):"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:
        print("Weekend")
    case _: #default
        print("Invalid day")