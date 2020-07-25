#Python For Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages,
# and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

#Print each name in a name list:
#The for loop does not require an indexing variable to set beforehand.
name =["Kiran","Ram","Bhuvan"]
for x in name:
    print(x)
#Looping Through a String
for x in "Bangalore":
    print(x)
#The break Statement

#With the break statement we can stop the loop before it has looped through all the items:

name =["Kiran","Shyam","Ram","Bhuvan"]
for x in name:
  print(x)
  if x == "Ram":
   break



#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#The range() Function
#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.
for x in range(6):
  print(x)
#The range() function defaults to increment the sequence by 1, however it is possible to specify
# the increment value by adding a third parameter: range(2, 30, 3):

for x in range(2, 50, 10):
  print(x)
#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Nested Loops
#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
   for y in fruits:
       print(x,y)

#The pass statement

for x in [0,1,2]:
    pass
#The pass statement is a null operation; nothing happens when it executes.