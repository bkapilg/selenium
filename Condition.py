#Python If ... Else
#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#These conditions can be used in several ways, most commonly in "if statements" and loops.
#An "if statement" is written by using the if keyword.
#if statement:
num1 = 31
num2 = 20
if num1>num2:
   print("num1 is greater then num2")

#Indentation
#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.
#Elif
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 45
if b > a:
    print("b is greater than a")
elif a == b:
  print(" a and  b are equal")
#Else
#Else
#The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a ==b:
    print("a and b are eqaual")
else:
    print("a is greater than b")

#Short Hand If
#If you h   ave only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")
#And-
#The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b =33
c =500
if a > b and c > a:
    print("both condition are true")
#OR-
#The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
   print("at least one condition are true")
#Nested if
x = 41

if x > 10:
   print("above ten",)
if x > 100:
   print("but not above 20!")

else:
    print("but not above 20.")

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement
# to avoid getting an error.
a = 33
b = 200

if b > a:
   pass




