#Create one variable of each type: int, float, str, bool, None. Print each value with its type.
num1 = 10
num2 = 1.203
string = 'Hello'
is_True = False
nothing = None
print(num1,num2,string,is_True,nothing)

#Take the string "Python" and print its first letter, last letter, and the slice "tho".
python = "Python"
print(python[0])
print(python[-1])
print(python[2:5])

#Convert "3.7" to a float and print it. Convert that float to an int and print it. Convert 123 to a str and print its type.
decimal = "3.7"
print(decimal,type(decimal))
as_float = float(decimal)
print(as_float,type(as_float))
as_int = int(as_float)
print(as_int,type(as_int)) # .7 was removed

#Print bool() of each: 0, 1, -5, "", "False", [], None.
zero = 0
positive_num = 1
negative_num = -5
empty_str = ""
false_str = "False"
empty_list = []
no_value = None
print(bool(zero),bool(positive_num),bool(negative_num),
      bool(empty_str),bool(false_str),bool(empty_list),bool(no_value))

#Create one list, one tuple, one set, and one dict, each holding at least three items.
num_list = [1,2,3]
num_tuple = (1,2,3)
num_set = {1,2,3}
num_dict = {'a':1,'b':2,'c':3}
print(num_list,num_tuple,num_set,num_dict)