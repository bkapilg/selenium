#Python Lists
#Python Collections (Arrays)

#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#A list is a collection which is ordered and changeable.
# In Python lists are written with square brackets.

mylist = ["anusha", "chelvi", "mytheli"]
print(mylist)

#Access items
print(mylist[1])
#Negative indexing means beginning from the end, -1 refers to the last
# item, -2 refers to the second last item etc.
print(mylist[-1])

#Range of Indexes
mylist = ["Anusha", "Chelvi", "Mythili","Nithya","Arun","Vaishnavi"]
#The search will start at index 2 (included) and end at index 5 (not included)
print(mylist[2:5])
#This example returns the items from index -4 (included) to index -1 (excluded)
print(mylist[-4:-1])
#Change Item Value
#To change the value of a specific item, refer to the index number:
mylist = ["Anusha", "Chelvi", "Mythili","Nithya","Arun","Vaishnavi"]
mylist[1] = "banu"
print(mylist)

#Loop Through a List
mylist = ["Anusha", "Chelvi", "Mythili","Nithya","Arun","Vaishnavi"]
for x in mylist:
    print(x)
#Check if Item Exists

mylist = ["Anusha", "Chelvi","Mythili","Nithya","Arun","Vaishnavi"]

if "kartik" in mylist:
  print("Yes, 'kartik' exists")
  #List Lenght
  # To determine how many items a list has, use the len() function:
mylist = ["Anusha", "Chelvi","Mythili","Nithya","Arun","Vaishnavi"]
print(len(mylist))

##Add Items
#To add an item to the end of the list, use the append() method:
mylist = ["Anusha", "Chelvi", "Mythili","Nithya","Arun","Vaishnavi"]
mylist.append("kartik")
print(mylist)
#To add an item at the specified index, use the insert() method:
mylist1 = ["Anusha", "Chelvi", "Mythili","Nithya","Arun","Vaishnavi"]
mylist1.insert(2,"EMe")
print(mylist1)
#Remove Item
#There are several methods to remove items from a list:
mylist1 = ["Anusha", "Chelvi", "Mythili","Nithya","Arun","Vaishnavi"]
mylist1.remove("Chelvi")
print(mylist1)
#The pop() method removes the specified index, (or the last item if index is not specified):

mylist1 = ["Anusha", "Chelvi", "Mythili","Nithya","Arun"]
mylist1.pop(2)
print(mylist1)
thislist = ["apple", "banana" "orange"]
thislist.remove('apple')
print(thislist)

 #delete list
thislist = ["rajesh", "john" , "bob"]
del thislist
print(thislist)