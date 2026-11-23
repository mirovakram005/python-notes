#Given a = 23 and b = 6, print the result of a + b, a - b, a * b, a / b, a // b, a % b, and a ** b.
a = 23
b = 6
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#Predict, then check: -7 // 2, -7 % 3, 7 % -3, 2 ** -1, -2 ** 2, and (-2) ** 2. Add a comment on any result that surprised you.
print("--------------------------------------")
print(-7 // 2)
print(-7 % 2)
print(-7 % -3)
print(2 ** -1)
print((-2) ** 2)

#Create number = 17. Use the % operator to print True if it's even and False if it's odd. Then change the number to 20 and check again.
print("--------------------------------------")
number = 20
print(number % 2 == 0)

#Start with x = 10. Using only +=, -=, *=, /=, //=, %=, and **= (one after another, in that order, with the value 2 each time), print x after each step.
print("--------------------------------------")
x = 10
x += 2
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2
print(x)
x //= 2
print(x)
x %= 2
print(x)
x **= 2
print(x)

#Create age = 25. Print whether it's greater than 18, whether it equals 30, whether it's not equal to 25, and whether it's between 18 and 30 using a chained comparison.
print("--------------------------------------")
age = 25
print(age > 18)
print(age == 30)
print(age != 25)
print(18 <= age <= 30)

#Create has_ticket = True and is_adult = False. Print the result of has_ticket and is_adult, has_ticket or is_adult, and not has_ticket. Then print "" or "Guest" and "hi" and "bye", and explain in a comment why they return those values.
print("--------------------------------------")
has_ticket = True
is_Adult = False
print(has_ticket,is_Adult)
print(has_ticket and is_Adult)
print(has_ticket or is_Adult)
print(not is_Adult)
print("" or "Guest") #returns Guest, because it is not empty string
print("hi" and "bye") #returns bye, because both strings is not empty, and operator returns last value

#Create text = "Python programming" and numbers = [1, 2, 3, 4, 5]. Print whether "Python" is in text, whether "java" is in text, whether 3 is in numbers, and whether 10 is not in numbers.
print("--------------------------------------")
text = "Python programming"
numbers = [1,2,3,4,5,6]
print("Python" in text)
print("jave" in text)
print(3 in numbers)
print(10 not in numbers)

#Create a = [1, 2, 3], b = [1, 2, 3], and c = a. Print a == b, a is b, and a is c. Add a comment explaining the difference between == and is.
print("--------------------------------------")
a = [1,2,3]
b = [1,2,3]
c = a
print(a is b)
print(a is c) #Are these two variables pointing to same object in memory
print(a == b) #Do these variables have the same value
