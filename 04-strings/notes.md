# Strings in Python 

## What is a string ? 
A string (str) is a sequence of characters: letters, digits, symbols, spaces, emoji. Strings are immutable, once created can't be changed.
Every charcter has its own index. 

```py
a = 'single quotes'
b = "double quotes"
c = """triple double quotes
can span several lines"""
d = '''triple single quotes
also work'''
e = ""                   # empty string
f = str(123)             # "123" (converted from a number)
```

## Escape sequence(последовательности)

|Sequence| Meaning | Example |
|--------|---------|----------|
|\\      | Backslash (\)    |**"C:\\Users\\Name" → C:\Users\Name**|
|\'	 | Single quote (') | **'It\'s fine' → It's fine**     |
|\"	 | Double quote (") | **"He said \"Hi\"" → He said "Hi"**|
|\n      | New Line         |**Hello "next line"  World** |
|\t      | Tab space        |**Name:\tAdam → Name:   Adam **|
|\r	 | Carriage return  |**abc\rX → Xbc** |


```py
print("Line 1\nLine 2")
print("Name:\tAdam")
print("C:\\Users\\Sally")
```
### Raw strings
if we put **r** before the quotes and backslashes are not treated as escapes. This is useful for Windows paths.
```py
print(r"C:\Users\newfile")
```

## Indexing
Each character has a position which called index, and it starts from 0. The negative indexes start counting from end.

| P | Y | T | H | O | N |
|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 |
|-6 |-5 |-4 |-3 |-2 | -1|

```py
p = "Python"
print(p[0])
print(p[4])
print(p[-2])
print(p[-4])
print(p[10]) #Error
```

## Slicing 
Format: p[start:stop:step]
- start -> where to begin slicing(element also included)
- stop -> where to end(element is not included)
- step -> how many elements to skip(default 1)
slices always creates new sting
```py
p = "Python"
p[0:3]      # "Pyt"
p[2:]       # "thon"    (from index 2 to the end)
p[:2]       # "Py"      (from the start up to index 2)
p[:]        # "Python"  (a full copy)
p[-3:]      # "hon"     (last 3 characters)
p[::2]      # "Pto"     (every second character)
p[::-1]     # "nohtyP"  (reversed)
p[1:5:2]    # "yh"
```

## Sring formatting 
string formatting has been added starting from python 3 version. Previously they used %s(for strings)
%d(for integers) and %f(floating point numbers).
```py
print("Value: %s" % 42)        # Value: 42
print("Flag: %s" % True)       # Flag: True
age = 25
print("I am %d years old" % age)
p = 3.14159265
print("%.2f" % p)     # 3.14
print("%.0f" % p)     # 3
print("%.4f" % p) 
```
**format()**
```py
print("{} is {}".format("Sam",20))
name = "Sam"
age = 25
print("{} is {}".format(name,age))
p = 3.12159265
print("{:.2f} is Pi".format(p))
```

f-strings startting from python 3.6+ version.
```py
name = "Sam"
age = 20
print(f"{name} is {age} years old")
print(f"Next year: {age + 1}")
p = 3.14159265
print(f"{p:.2f}")          # "3.14"        (2 decimals)
print(f"{1000000:,}")       # "1,000,000"   (thousands separator)
print(f"{0.256:.1%}")       # "25.6%"       (percentage)
print(f"{42:05d}")          # "00042"       (pad with zeros, width 5)
print(f"{'hi':>6}")         # "    hi"      (right-align in width 6)
print(f"{'hi':<6}")         # "hi    "      (left-align)
print(f"{'hi':^6}")         # "  hi  "      (center)
print(f"{'hi':*^8}")        # "***hi***"    (fill with *)
print(f"{255:b}")           # "11111111"    (binary)
print(f"{255:x}")           # "ff"          (hex)
```
## String methods
string methods are used to manipulate with string. they return a new string, not changing the original.
```py
text = "Hello World"
print(text.upper())               #HELLO WORLD
print(text.lower())               #hello world	
print("hello world".capitalize()) #Hello world
print("hello world".title())      #"Hello World"
print("Hello".swapcase())         #"hEllo"
```
**_strip()_** -> removes white space and only from the end, not from the middle
```py
"  hi  ".strip()        # "hi"
"  hi  ".lstrip()       # "hi  "
"  hi  ".rstrip()       # "  hi"
"xxhixx".strip("x")     # "hi"
```
- **_find()_** -> Searches from the left and returns the starting index. If the substring isn't found, it safely returns -1.
- **_rfind()_** -> Searches from the right ("reverse find") and returns the last starting index. Returns -1 if missing.
- **_index()_** -> Works identically to .find(), except if the substring is missing, it crashes with a ValueError instead of returning -1
- **_count()_** -> Checks how many times the word or letter appears.
- **_startswith()_** -> Checks whether the string begins with exact sequence of characters and returns a boolean.
- **_endswith()_** -> Checks whether the string end with exact sequence of characters and returns boolean(True of False)
```py
fruit = "banana"
fruit.find("an")        # 1   (first position, or -1 if not found)
fruit.rfind("an")       # 3   (last position)
fruit.index("an")       # 1   (same as find, but raises ValueError if missing)
fruit.count("a")        # 3
fruit.startswith("ba")  # True
fruit.endswith("na")    # True
```
- **_replace()_** -> replace a character with the given one.
- **_split()_** -> breaks a string into a list of smaller strings (substrings) based on a separator.
- **_join()_** -> Opposite to split, it is used to join list,tuple,set of strings and put them together in to single string, placing separator between very elemnt.
```py
"banana".replace("a", "o")        # "bonono"
"banana".replace("a", "o", 2)  
"a,b,c".split(",")            # ["a", "b", "c"]
"a b   c".split()             # ["a", "b", "c"]  (any whitespace, no empties)
"a,b,c".split(",", 1)         # ["a", "b,c"]     (max 1 split)
", ".join(["a", "b", "c"])    # "a, b, c"
"".join(["a", "b", "c"])      # "abc"
```

- **_isalpha()_** -> Checks a string consists exclusively of alphabetic characters with no spaces, digits, or punctuation.
- **_isdecimal()_** -> Checks whether a string consists exclusively of standard base-10 decimal digits (0 to 9).
- **_isdigit()_** -> Checks whether a string consists of numeric digit characters,
- **_isupper()_** ->  Checks all case-sensitive (alphabetic) characters in a string are in uppercase, while ignoring non-alphabetic characters.
- **_islower()_** -> Checks whether all characters in a string are in lowercase or not.
```py
print("Python".isalpha())       # True  (only letters)
print("Hello world".isalpha())  # False (contains a space)
print("".isalpha())             # False (empty string)
print("2026".isdecimal())       #True
print("3.14".isdecimal())       # False (contains a decimal point)
print("-42".isdecimal())        # False (contains a minus sign)
print("2026".isdigit())         # True  (standard digits)
print("HELLO".isupper())        # True  (all letters are uppercase)
print("Hello".isupper())        # False (contains lowercase letters)
print("hello".islower())        # True  (all letters are lowercase)
print("Hello".islower())        # False (contains an uppercase letter)
```

