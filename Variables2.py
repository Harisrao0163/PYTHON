#                                        Assign multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

# Assign the single value to multiple variables
x = y = z = "Orange"

print(x)
print(y)
print(z)


# Unpack a collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple" , "bannana" , "cherry"]
x ,y , z = fruits
print(x)
print(y)
print(z)

#                                                       Output Variables


fruits = ["apple" , "bannana" , "cherry"]
x ,y , z = fruits
print(x ,y , z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)# In the print() function, you output multiple variables, separated by a commas.

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)# In the print() function, you can also use the + operator to output multiple variables. This will concatenate (combine) the variables.
# Note: When using the + operator, make sure to include spaces if needed.
#                                                           POINT

#For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

"""x = 5
y = "John"
print(x + y)"""

#This will produce an error because you are trying to combine a string (y) with a number (x). To fix this, you can convert the number into a string:

#  Solution  :

#The best way to output multiple variables in the print() function is to separate them with "commas", which even support different data types:

x = 5
y = "John"
print(x , y)