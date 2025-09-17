#                                                              Python Numbers

#There are three numeric types in Python:
#int
#float
#complex

#To verify the type of any object in Python, use the type() function:

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#                                                                    Int
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
#                                                                    Float
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
#Float can also be scientific numbers with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#                                                                   Complex
#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#                                                                 Type Conversion
#You can convert from one type to another with the int(), float(), and complex() methods:

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#                                                                  Random Number
#Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))
#This example returns a random number between 1 and 9.
