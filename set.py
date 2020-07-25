#Set
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
#Create a Set:

thisset = {"Java","Python","Ruby","Selenium"}
print(thisset)
#Sets are unordered, so you cannot be sure in which order the items will appear.
#Access Items
#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.

thisset={"Java","Python","Ruby","Selenium"}
for x in thisset:
    print(x)
#Check if "Python" is present in the set:
thisset={"Java","Python","Ruby","Selenium"}
print("java in thisset")

#Change Items
#Once a set is created, you cannot change its items, but you can add new items.
#Add Items
#To add one item to a set use the add() method.
#To add more than one item to a set use the update() method.
thisset={"Java","Python","Ruby","Selenium"}
thisset.add("c++")
print(thisset)

#Add multiple items to a set, using the update() method:
thisset={"Java","Python","Ruby","Selenium"}
thisset.update(["BDD","AWS"])
print(thisset)

#Get the Length of a Set
#To determine how many items a set has, use the len() method.
thisset={"Java","Python","Ruby","Selenium"}
print(len(thisset))
#Remove Item
#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
#Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.

#The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x  =  thisset.pop()
print(x)
#Sets are unordered, so when using the pop() method, you will not know which item that gets removed
#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
x = thisset.clear()
print(thisset)


#Join Two Sets
#There are several ways to join two or more sets in Python.

#You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another:

#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Both union() and update() will exclude any duplicate items.

#The set() Constructor
#It is also possible to use the set() constructor to make a set.
thisset = set (("apple", "banana", "cherry"))
print(thisset)
