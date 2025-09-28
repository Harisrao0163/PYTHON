#                                                                     LOOPS
#strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
 print (x)
#                                                                  STRING LENGTH
#To get the length of a string, use the len() function
a = "Hello, World!"
print(len(a))
#                                                                   CHECK STRING
txt = "The best things in life are free!"
print("things"in txt)

#Use it in an if statement:

txt = "The best things in life are free!"
if "things" in txt:
   print("yes 'things' is present.")

'''Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if '''
a = 33
b = 200

if b > a:
  print("b is greater than a")
#In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a.
# As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

#                                                                Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement:

txt = "The best things in life are free!"
if "expensive" not in txt:
     print("no,'expensive' not in txt")



