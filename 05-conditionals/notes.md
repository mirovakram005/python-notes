# Conditionals in Python

## What is conditional ? 
Conditional statements are used to control the flow of execution in a program based on specific conditions.
Conditionals execute blocks of code depending whether the condition returns True or False.

## If Statement

```py
if condition:
        #code that runs only when condition is True 
```

For Example

```py
age = 20
if age > 18: 
    print('You are an adult')

#------------------------------

temperature = 30
if temperature > 25:
           print('It is hot')
print('This line always runs')
```
Rules you must follow
- The code inside the block must be indented (the standard is 4 spaces)
- The block ends when the indentation goes back
Python uses indentation to define blocks. There are no { } braces. Wrong indentation gives an IndentationError.


## If/Else
When the if condition returns false, then the block of code which is inside **else** will run.
So basically if condition is False **else** will run.
```py 
if condition: 
    block of code
else:
    block of code

#-----------------------------

age = 17 

if age > 18: 
     print("You're adult")
else:
     print("You are not adult")

```


## If/Elif/Else
To use more than one condition we use keyword **elif**. It checks the conditions in order.
```py
if condition_1:
     block of code
elif condition_2: 
     block of code
elif condition_3:
     block of code
else:
     block of code

#-----------------------------

score = 75
if score > 90:
     print("A")
elif score >= 80:
     print("B")
elif score >= 70
     print("C")
else:
     print("F")
```

## If/Else and Logical Operators | Membership
```py
age = 25
has_id = True

if age >= 18 and has_id:    # has_id == True
    print("Entry allowed")

if age < 13 or age > 65:
    print("Discount")

if not has_id:
    print("Show your ID")

#-----------------------------

vowels = "aeiou"
letter = "e"
if letter in vowels:
       print("Vowel")

if letter not in vowels:
       print("Constant")
```

## Nested Conditionals
An if inside another if.
```py
age = 20
has_ticket = True

if age > 18:
    if has_ticket == True:
         print("Welcome")                 
     else:
         print("Buy a ticket")
else:
    print("Too young")
```


## The ternary operator(one-line if/else)
If you have a simple condition you can use ternary operater, otherwise it is recommended to use the normal if. 
```py
# value_of_true if condition else value_of_false
age = 20;
status = "adult" if age > 18 else "minor"
print(status)
```

## Match/Case (Python 3.10+)
A cleaner way to compare one value against many options. It's similar to switch in other languages, but more powerful.
```py

num = 3

match num:
    case 1:
       print("This is number 1")
    case 2:
       print("This is number 2")
    case 3:
       print("This is number 3")
    case 4:
       print(f"This is number 4")

#-----------------------------

day = Tuesday

match day:
    case "Monday": 
          print(f"Today is {day}")
    case "Tuesday":
          print(f"Today is {day}")
    case "Friday":
          print(f"Today is {day}")
    case "Sunday":
          print(f"Today is {day}")
```
