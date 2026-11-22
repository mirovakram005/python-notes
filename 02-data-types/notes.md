# Data Types in Python 

## What is data type? 
A data type tells a programming langauge what kind of value something is. It defines what kind of value a variable can store
and what operations can be performed on it.

## Built in Types in Python
 
| Category | Types |
| --- | --- | 
| Numbers  | **int**, **float**, **complex** |
| Text     | **str** |
| Boolean  | **bool** |
| Nothing  | **NoneType** |
| Sequence(последовательность) | **list**, **tuple(кортеж)**, **range** |  
| Mapping  | **dict** | 
| Sets     | **set**, **frozenset** | 
| Binary   | **bytes**,**bytearray** |

Also data types split into two part:
**Immutable** can not change its value once created(any modification/change actually creates a new object in memory):
- int,float,bool,str,tuple,None

**Mutable** can change its value once created:
- list,dict,set

## Numbers 
**int** represents whole numbers(positive,negative,zero) in Python.Python integers has no limit, apart from your memory.
 
```py
a = 42
b = -2
c = 0
d = 1_000_000 #underscope makes big numbers readable
```

**float** represents decimal number.Floats are slightly imprecise. if we do 01 + 0.2 it will give 0.30000000000000004.
This happens in every programming language not only in Python.

```py
pi = 3.14
a = 20.5
b = 2.5e - 3 # scientific notation = 0.0025
```

**complex** represents complex numbers.

```py
a = 3 + 4j
```
## String 
**str** represents text in Python. We can use single, double and triple quotes. Strings are immutable. Each character in string has an index,starting from 0.

```py
a = 'Hello'
b = "Hello"
c = """ Hello """
d = 'Hello' + 'World' #Concatination
print(a[0]) #H
print(a[-1]) #o
print(a[0:3]) #Hel (slicing)
print(d)
```
## Boolean 
**bool** represents True or False values.In Python 0 means False and 1 means Truth.

```py
is_Active = True
is_Adult = False
```
## None
**None** represent nothing or no value in Python. 

```py

result = None

```

## Collections
We will study each one separately later, for now we will just take a look what they are.

```py
a = [1,2,3,4] #list
b = (1,2,3,4) #tuple
c = {1,2,3}   #set
d = {"A": 1, "B": 2} #dict
```

## Type Conversion
To convert data type, we use **_int()_**,**_float()_**,**_str()_**,**_bool()_**,**_list()_**, etc..
- **_type()_** -> used to check the data/values type.

```py
a = '200'
b = 100
print(type(a))
a = int(a)
print(type(a))
print(type(str(b)))
```



