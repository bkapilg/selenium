#Tuple
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

#Create a Tuple:
mytuple = ("Harry", "John", "Ben")
print(mytuple)
#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
mytuple = ("Harry", "John", "Ben")
print(mytuple[1])
mytuple = ("Harry", "John", "Ben","Dorian","Obenza","Kenny")
print(mytuple[2:5])
#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the tuple:
mytuple = ("Harry", "John", "Ben","Dorian","Obenza","Kenny")
print(mytuple[-4:-1])
#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable
#But there is a workaround. You can convert the tuple into a list, change the list,
# and convert the list back into a tuple.

mytuple = ("Harry", "John", "Ben","Dorian","Obenza","Kenny")
newlist = list(mytuple)
newlist[1] = "Yep"
mytuple=tuple(newlist)
print(mytuple)
#Loop Through a Tuple
mytuple = ("Harry", "John", "Ben","Dorian","Obenza","Kenny")
print (mytuple)
for x in mytuple:
    print(x)

#Check if Item Exists
mytuple = ("Harry", "John", "Ben","Dorian","Obenza","Kenny")
if "Nekki" in mytuple:
    print("Yes!")
#Tuple Length
mytuple = ("Harry", "John", "Ben","Dorian","Obenza","Kenny")
print(len(mytuple))
#Create Tuple With One Item
#To create a tuple with only one item, you have add a comma after the item,
# unless Python will not recognize the variable as a tuple
mytuple = ("harry,")
print(mytuple)

#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
thistuple = (("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#Remove items
#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:

#Remove Items
#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
thistuple = (("apple", "banana", "cherry"))
del thistuple
print(thistuple)

