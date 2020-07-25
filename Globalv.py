#Example 8
#GLOBAL VARIABLES
#Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
x = "Prem"
def myfunc():
 print("My Name is " + x)
myfunc()

#The global Keyword
#Normally, when you create a variable inside a function, that variable is local,
# and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.
def myfunc():
 global x
 x = "fantastic"


myfunc()

print("Python is " + x)

#Also, use the global keyword if you want to change a global variable inside a function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)