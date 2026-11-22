# Variables in Python 

## What is variable? 
A variable is a name that points(refers) to a value/data in computer memory(RAM). We can use this variable by name to read or modify the value. 

```py
age = 25
name = 'Sam'
```
Here the _age_ and _name_ are the variable names and the _"="_ equal sign is assignment operator. It means to store the value/data in the variable.
Equal sign in Python is not the same in Math.

## Creating Variables(Declaring Variables)
Python hasn't any keyword for declaring variables like other programming languages(no var,let,etc..). You decalre one the moment you assign value to it.
Python is a dynamically typed language which means you don't need to declare the variable's type. Python automatically determines it for you at the runtime. 

```py
x = 50 #int
y = "Hello"
```

## Naming rules 
- Variable name can contain letters,digits and underscore "_"
- Variable name can't start with digit, must start with letter or underscore
- No spaces or special characters(-,$,@) in variable name 
- Variable name is case-sensitive, _age_, _Age_ and _AGE_ are different variables
- Variable name can not contain keywords(if,else,while,for,etc...)

Valid:

```py
user_name = 'Scot'
user_age = 25
user_card_id = 2
is_Active = True
_count = 10
 ```
Invalid:

```py
user-name = 'Addy'
class = 'A'
user@card@id = 10
```
## Naming Conventions(style)
Naming conventions are standardized rules or community guidline for choosing names for variables,functions,classes and constants. 
- **snake_case** -> most used style in Python language, used for variables and functions.
- **UPPER_CASE** -> used for constants.
- **PascalCase** -> used for classes.

## Printing variables
- **_print()_** -> is a built-in function used to print(show) variable's value in console.
- **_input()_** -> is a built-in function used to take user input as a string(if user entered number, we need Type conversion to convert string to int)
- **_len()_** -> is a built-in function used to find the variable's length

```py
print('Hello World!')
print('Hello','   ', 'World')
user_name = input('Enter your name: ')
print(user_name)
print(len(user_name)) #length
```
#### Reassigning and updating

```py
score = 20
score = 50 // reassign
score = score + 10
score += 5 //updating
```
#### Multiple assignment 

```py
a,b,c = 1,2,3 # different values
x = y = z = 0 # different variables, same value
```
- **Global variable** -> created outside function called global
- **Local variable** -> created inside function called local

## Comments
Commetns are non-executable notes used to describe or explain what a specific block of code does.
- **#** -> single-line comment
- **"""  """** -> multi-line comment
