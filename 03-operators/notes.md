# What is an operator? 
An operator is a symbol or keyword that perform an action on values(called operands).

```py
3 + 2 # + is operator, 3 and 2 are operands
not True # keyword also can be operatos
```
## Types of Operators
 
|Category|Operators|
|--------|---------|
|**Arithmetic**|**+**,**-**,*,**/**,**//**,**%**, **| 
|**Assignment**|**=**,**+=**,**-=**,*=,**/=**,**//=**,**%=**,**&=**,**^=**, **<<=**, **>>=**, **:=**,**=|
|**Comparison**|**= =**, **!=**, **>**, **<**, **>=**, **<=**|
|**Logical**|**and**, **or**, **not**|
|**Membership**|**in**, **not in**|
|**Identity**|**is**,**is not**|
|**Bitwise**|**&**, **^**,**~**,**<<**,**>>**|

## Arithmetic operators

Arithmetic operators used to perform mathimetic operations on operands.
 
| Operator | Name |
|--------- |------|
| **+**	   |Addition|	
| **-**	   |Subtraction|	
| *	   |Multiplication|	
| **/**	   |True division|	
| **//**   |Floor division|	
| **%**	   |Module|	
| **	   |Power|		

```py
print(10 + 5) 
print(10 - 5)
print(10 * 5)
print(10 / 5) # division -> returns a float 
print(10 // 5) # floor division -> returns integer and down toward negative infinity 
print(10 % 5) # returns remainder, also can use floats
print(10 ** 2) # (10 * 10) evaluates to  100 
```
## Assignment Operators
Python hasn't increment(++) and decrement(--) operators, instead it uses _+=1_ and _-=1_.

|Operator    |Same as|
|------------|-------|
|**x += 3**  |x = x + 3|
|**x -= 3**  |x = x - 3|
|x *= 3	     |x = x * 3|
|**x /= 3**  |x = x / 3|
|**x //= 3** |x = x // 3|
|**x %= 3**  |x = x % 3|
|x ****= 3** |x = x ** 3| 

and so on

```py
X = 3
x += 1 #4
x -= 1 #3
x *= 2 #6
x /= 3 #2.0
x //= 2 #1
```

## Comparison operators 
Comparison operators used for comparing two or more values. Comparison Operators always return boolean type(True or False).

|Operator|Meaning|
|--------|-------| 	
|**= =** |equal|	
|**!=**	 |not equal|	
|**>**	 |greater|		
|**<**	 |less|		
|**>=**	 |greater or equal|
|**<=**	 |less or equal|

```py
print(10 == 5) #False
print(10 != 5) #True
print(10 > 5)  #True
print(10 < 5)  #False
print(10 >= 5) #True
print(10 <= 5) #False
print(5 == 5.0)#True
```
## Logical operators
Logical operators used to combine conditionals(boolean).

|Operator|Meaning|
|--------|-------|
|**and** |Returns **True** if both sides are **True**|
|**or**	 |Returns **True** if at least one condition(side) is **True** |
|**not** |Reverse the boolean value(**True** -> **False**, **False** -> **True**)|

| A | B | A and B | A or B |
| :--- | :--- | :--- | :--- |
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

```py
print(10 > 5 and 20 > 10) #True
print(10 < 5 or 5 < 10) #True
print(not False) #True
```

## Membership operators 
Membership operators used to check whether a value or element exist in collection, returning True or False.
- **in** -> verify if the value exist or found inside a collection.
- **not in** -> verify if the value not found inside collection.
In dictionary Membership operators check keys, not values.

```py
print("a" in "apple") #True
print(3 in [1,2,3])   #True
print(4 in (2,5,6))   #False
print("name" not in {"name":"Anna"}) #False
```

## Identity operators
Identity operators verify whether two values/variables refers to same Object in computer memory.
- **is** -> if both variables refer to the same object in computer memory,then returns True. Not recommended to use for numbers or strings.
- **is not** -> if both variables refer to different objects in computer memory, then it returns False.
- **=** -> used for values
- **_id()_** -> shows an object's identity.

```py 
a = [1,2]
b = [1,2]
c = a
d = b
print(c is a) #True
print(b is d) #False
print(a is not d) #True
print(b is not a) #True
print(C is d) #False
```

