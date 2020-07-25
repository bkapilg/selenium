#Python also has a super() function that will make the child class inherit all the methods and properties from its parent

#By using the super() function, you do not have to use the name of the parent element,
# it will automatically inherit the methods and properties from its parent.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()
#Add properties
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
      print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  # Add Methods
  class Person:
      def __init__(self, fname, lname):
          self.firstname = fname
          self.lastname = lname

      def printname(self):
          print(self.firstname, self.lastname)

  class Student(Person):
      def __init__(self, fname, lname, year):
          super().__init__(fname, lname)
          self.graduationyear = year

      def newmethod(self):
          print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

  x = Student("Mike", "Olsen", 2019)
  x.newmethod()

  # If you add a method in the child class with the same name as a function in the parent class,
  # the inheritance of the parent method will be overridden.



