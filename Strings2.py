#                                                            Slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string

b = "Hello, World!"
print(b[2:5])

#                                                      Slice From the Start
#By leaving out the start index, the range will start at the first character:

b = "Hello, World!"
print(b[:5])

#                                                      Slice From the End
#By leaving out the end index, the range will go to the last character:

print(b[7:])

#                                                      Negative Indexing
#Use negative indexes to start the slice from the end of the string:

print(b[-6:-1])

#This example returns the characters from index -6 to index -1 (not included):
#Note: The character at the end index is not included.

#                                                          Upper Case
#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
#                                                          Lower Case
#The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

#                                                          Remove Whitespace
#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#                                                          Replace String
#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

#                                                          Split String
#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#                                                          concatination 
#To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a + b
print(c)

#or
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#                                                           F-Strings
#Python also has a method called f-strings, which is a way to format strings.
#You can add a placeholder by using curly brackets {}.

c = f"{a} {b}"
print(c)

#A placeholder can include a modifier to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

price = 49.99
txt = f"The price is {price:.2f} dollars"
print(txt)

#The result will be:
#The price is 49.99 dollars
#Note: You cannot use f-strings in versions lower than Python 3.6.
#Note: The f in f-strings stands for formatted.
#Note: You can add the letter F before the string as well.
#The result will be the same:

price = 49.99
txt = F"The price is {price:.2f} dollars"
print(txt)

#                                                       Escape characters
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#The escape character allows you to use double quotes when you normally would not be allowed:
#Another escape character is a backslash \ followed by an n, which is used to insert a new line in a string:

txt = "Hello\nWorld!"
print(txt)

#The result will be:
#Hello
#World!
#                                                       METHODS OF STRING

# Method	                        Description
'''
capitalize()	                    Converts the first character to upper case
casefold()	                      Converts string into lower case
center()                        	Returns a centered string
count()                           Returns the number of times a specified value occurs in a string
encode()                        	Returns an encoded version of the string
endswith()	                      Returns true if the string ends with the specified value
expandtabs()                    	Sets the tab size of the string
find()	                          Searches the string for a specified value and returns the position of where it was found
format()                         	Formats specified values in a string
format_map()	                    Formats specified values in a string
index()	                          Searches the string for a specified value and returns the position of where it was found
isalnum()	                        Returns True if all characters in the string are alphanumeric
isalpha()	                        Returns True if all characters in the string are in the alphabet
isascii()	                        Returns True if all characters in the string are ascii characters
isdecimal()	                      Returns True if all characters in the string are decimals
isdigit()	                        Returns True if all characters in the string are digits
isidentifier()                   	Returns True if the string is an identifier
islower()	                        Returns True if all characters in the string are lower case
isnumeric()                     	Returns True if all characters in the string are numeric
isprintable()                   	Returns True if all characters in the string are printable
isspace()	                        Returns True if all characters in the string are whitespaces
istitle()	                        Returns True if the string follows the rules of a title
isupper()	                        Returns True if all characters in the string are upper case
join()	                          Joins the elements of an iterable to the end of the string
ljust()                          	Returns a left justified version of the string
lower()                         	Converts a string into lower case
lstrip()                        	Returns a left trim version of the string
maketrans()                     	Returns a translation table to be used in translations
partition()	                      Returns a tuple where the string is parted into three parts
replace()	                        Returns a string where a specified value is replaced with a specified value
rfind()	                          Searches the string for a specified value and returns the last position of where it was found
rindex()	                        Searches the string for a specified value and returns the last position of where it was found
rjust()                         	Returns a right justified version of the string
rpartition()                    	Returns a tuple where the string is parted into three parts
rsplit()                        	Splits the string at the specified separator, and returns a list
rstrip()	                        Returns a right trim version of the string
split()	                          Splits the string at the specified separator, and returns a list
splitlines()                     	Splits the string at line breaks and returns a list
startswith()	                    Returns true if the string starts with the specified value
strip()	                          Returns a trimmed version of the string
swapcase()	                      Swaps cases, lower case becomes upper case and vice versa
title()	                          Converts the first character of each word to upper case
translate()                     	Returns a translated string
upper()                         	Converts a string into upper case
zfill()                         	Fills the string with a specified number of 0 values at the beginning'''



