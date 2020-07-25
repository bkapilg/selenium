#Python Classes and Objects
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects

#Create a Class
#Create a class named MyClass, with a property named x:

class MyClass:
   x = 5
#objectname = classname()
p1 = MyClass
print(p1.x)

#The __init__() Function
#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when
# the object is being created:
class Person:
 def__init__(self, name, age)
       self.name = name
       self.age  = age
#objectname = classname()
p1 = person("ben" , 36)
print(p1.name)
print(p1.age)
#Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#Let us create a method in the Person class:
class Person:
    def__init__(self,name,age):
        self.name = name
        self.age  = age
    def myfunc(self):
       print("hello my name is" + self.name)

    p1 = person("john", 36)
    #objectname.methodname()
    p1.myfunc()
#The self Parameter
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any
# function in the class:

#Modify Object Properties
class person():
 def__init__(self,name,age):
    self.name = name
    self.age  = age
def myfunc(self):
    print("hello name is " + self.name)

p1 = person("john", 36)

p1.age = 40

print(p1.age)
