# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Code Reusability
# Transition and Readability
# Real world Relationship

# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# Create a Parent Class
# Create a class named Person, with firstname and lastname properties, and a printname method:

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = person("john", "doe")
x.printname()

#Create a Child Class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
 pass

x = Student("Mike", "Olsen")
x.printname()




#Add the __init__() Function
#So far we have created a child class that inherits the properties and methods from its parent.
#We want to add the __init__() function to the child class (instead of the pass keyword).
#The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

