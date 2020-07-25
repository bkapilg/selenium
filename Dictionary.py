#Dictionary
#A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
thisdict ={
    "Name": "Sheldon",
    "Age" : 10,
    "Country" :"US"

}
print(thisdict)
#Accessing Items
#You can access the items of a dictionary by referring to its key name,
# inside square brackets:

thisdict ={
    "Name": "Sheldon",
    "Age" : 10,
    "Country" :"US"
}
x = thisdict["Name"]
print(x)
#There is also a method called get() that will give you the same result:

x = thisdict.get("Name")
print(x)

#Change Values
#You can change the value of a specific item by referring to its key name:
thisdict = {"Name": "Sheldon", "Age": 10, "Country": "UK"}
print(thisdict)

#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.
#Print all key names in the dictionary, one by one:

for x in thisdict:
    print(thisdict[x])

#You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
  print(x)
  # Loop through both keys and values, by using the items() function:
for x,y in thisdict.items():
   print(x,y)

#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {"Name": "Sheldon", "Age": 10, "Country": "UK"}
if "Age" in thisdict:
      print("age exists")

#Dictionary Length
#To determine how many items (key-value pairs) a dictionary has, use the len() method.

print(len(thisdict))
#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a
# value to it:

thisdict = {"Name": "Sheldon", "Age": 10 ,"Country": "UK"}
thisdict["nickname"] = ["Shelly"]
print(thisdict)

#Remove dictionary
#Removing Items
#There are several methods to remove items from a dictionary:

#The pop() method removes the item with the specified key name
thisdict1 = {"Name": "Sheldon", "Age": 10, "Country": "UK"}
thisdict1.pop("Age")
print(thisdict1)

#The popitem() method removes the last inserted item
thisdict = {"Name": "Sheldon", "Age": 10, "Country": "UK","City": "Po"}
thisdict1.popitem()
print(thisdict)

thisdict = {"Name": "Sheldon", "Age": 10, "Country": "UK"}
thisdict.clear()
print(thisdict)
