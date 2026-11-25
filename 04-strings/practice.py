#Make three strings, one with single quotes, one with double quotes, and one with triple quotes spanning three lines. Print each one and its type()
a = 'hello'
b = "hello"
c = """Hello 
     World"""
print(a)
print(b)
print(c)
#In a single print() call, display this exactly (using \n, \t, \\, and \")
print(" Name: Ali\n Path: C:\\User\\Ali\n Quote: \"Python\" is fun")

#Create word = "Programming". Print the first letter, the last letter.
word = "Programming"
print(word[0])
print(word[-1])

#With the same word, print "Pro", "gram", the last 3 letters, every second letter, and the word reversed.
print(word[0:3])
print(word[3:7])
print(word[:-3])
print(word[::2])
print(word[::-1])

#Create text = " hello, Python world ". Print it after .strip(), .title(), and .replace("Python", "Go").
#Then print text itself and add a comment explaining why it didn't change. Finally, save a cleaned version in a new variable: stripped and in uppercase.
text = " hello, Python world "
text.strip()
text.title()
text.replace("Python","Go")
print(text) #it did not work cause string is immutable, and the methods create new string
print(text.strip())
print(text.title())
print(text.replace("Python","Go"))
print(text.upper())

#Using sentence = "banana bread is better than banana cake", print how many times "banana" appears,
# the position of the first "bread", whether it starts with "banana", whether it ends with "cake",
# and the result of .find("pizza"). Add a comment on what -1 means.
sentence = "banana bread is better than banana cake"
print(sentence.count("banana"))
print(sentence.find("bread"))
print(sentence.find("pizza")) # returns -1 cause it did not find it
print(sentence.startswith("banana"))
print(sentence.endswith("cake"))
