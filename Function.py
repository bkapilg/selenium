#Python Functions
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#Creating a Function
#In Python a function is defined using the def keyword:
def my_function():
  print("hello from a function")

#Calling a Function
#To call a function, use the function name followed by parenthesis
def my_function():
    print("hello from a function")
my_function()

#Parameters
#Information can be passed to functions as parameter.
#Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want,
# just separate them with a comma.
#The following example has a function with one parameter (fname). When the function is called, we pass along a first name,
# which is used inside the function to print the full name:
def my_function(fname):
  print(fname + "Acquinson")

my_function("java")
my_function("Anvas")
my_function("jeeva")
#Default Parameter Value
#The following example shows how to use a default parameter value.
#If we call the function without parameter, it uses the default value:

def my_function(country = "Norway"):
    print("i am from "+ country)

my_function("sweeden")
my_function("india")
my_function()
my_function("brazil")

#Passing a List as a Parameter
#You can send any data types of parameter to a function (string, number, list, dictionary etc.), and it will be treated as
# the same data type inside the function.
#E.g. if you send a List as a parameter, it will still be a List when it reaches the function:

def my_function(food):
    for x in food:
        print(x)
food = ["apple", "banana", "cherry"]
my_function(food)

#Return values
def my_function (x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#Keyword Arguments
#You can also send arguments with the key = value syntax.

#This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
    print("the youngest chid is" + child3)

my_function(child1 = "Eme",child2= "yip",child3= "Ben")
#Arbitrary Arguments
#If you do not know how many arguments that will be passed into your function, add a * before the
# parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

#If the number of arguments are unknown, add a * before the parameter name:
def my_function(*kids):
    print("the youngest child is" +kids[2])
my_function("jim","Toe","Harry")

#The pass Statement
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
    pass