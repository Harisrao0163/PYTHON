#                                                         Variables
x = 4
x = "Sally"
print(x) #this will show us the recent value of x which is "Sally"


#Casting
x = str(3)
y = int(3)
z = float(3)
e = complex(3)
#If you want to specify the data type of a variable, this can be done with casting.
print(x)
print(y)
print(z)
print(e)

#Get the type

x = 5
y = "John"
print(type(x)) #You can get the data type of a variable with the type() function
print(type(y))


#Case-Sensitive
a = 4
A = "Sally" #Variable names are case-sensitive.
print(a)
print(A)

"""                                          Variable Name
                                                RULES
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
                                           Python Keywords 
Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:

Keyword	                Description
and                 	A logical operator
as	                    To create an alias
assert	                For debugging
break	                To break out of a loop
class	                To define a class
continue	            To continue to the next iteration of a loop
def	                    To define a function
del                    	To delete an object
elif                	Used in conditional statements, same as else if
else	                Used in conditional statements
except	                Used with exceptions, what to do when an exception occurs
False	                Boolean value, result of comparison operations
finally                 Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	                    To create a for loop
from	                To import specific parts of a module
global	                To declare a global variable
if	                    To make a conditional statement
import              	To import a module
in                   	To check if a value is present in a list, tuple, etc.
is	                    To test if two variables are equal
lambda	                To create an anonymous function
None	                Represents a null value
nonlocal	            To declare a non-local variable
not	                    A logical operator
or	                    A logical operator
pass	                A null statement, a statement that will do nothing
raise	                To raise an exception
return	                To exit a function and return a value
True	                Boolean value, result of comparison operations
try	                    To make a try...except statement
while	                To create a while loop
with	                Used to simplify exception handling
yield	                To return a list of values from a generator"""

myvar = "John"
my_var = "John"
Myvar = "John"

print(myvar)
print(my_var)
print(Myvar) #Remember that variable names are case-sensitive


#Variable names with more than one word can be difficult to read.
#There are several techniques you can use to make them more readable

#    Camel case
myVariableName = "John" #Each word, except the first, starts with a capital letter
print(myVariableName)

#    Pascal case
MyVariableName = "John" #Each word starts with a capital letter
print(MyVariableName)

#    Snake case
my_variable_name = "John" #Each word is separated by an underscore character
print(my_variable_name)
