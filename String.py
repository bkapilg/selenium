#Python Strings
#String literals in python are surrounded by either single quotation marks, or double quotation marks
#'Vaishnavi' is the same as "Vaishnavi"

print("Vaishnavi")
print('Vaishnavi')

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string
a = "durge"
print(a)

#Multiline Strings
#You can assign a multiline string to a variable by using three double quotes or single quotes:
a= """Python is so easy to learn,
Start learning today,
Yeah! Beleive me ya."""
print(a)


#Strings are Arrays
a = "world!"
print(a[1])

#Slicing
b = "Durga!"
print(b[2:5])

#Negative Indexing
#Get the characters from position 5 to position 1, starting the count from the end of the string:
b = "RajeshKumar"
print(b[-5:-2])


#String Length
#The len() function returns the length of a string
a = "kritjika"
print(len(a))

#Python has a set of built-in methods that you can use on strings.
#The strip() method removes any whitespace from the beginning or the end:
a = " Jeera, Heera! "
print(a.strip())

#The lower() method returns the string in lower case:
a = "Nirajani!"
print(a.lower())

#The upper() method returns the string in upper case:
a = "Meera!"
print(a.upper())

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "j"))


#The split() method splits the string into substrings if it finds instances of the separator
a = "Meera, Kumar!"
a.split(",")

#To check if a certain phrase or character is present in a string, we can use the keywords in or not in
txt = "The rain in Spain stays mainly in the plain"
x = "ain not in txt"
print(x)
#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.
a = "jim"
b = "jam"
c =a+b
print(c)

#To add a space between them, add a " ":

a = "Durga"
b = "Ethiraj"
c = a  +" "+ b
print(c)

#String Format
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are

age = 25
txt = "My name is Priya, and I am {}"
print(txt.format(age))


#The format() method takes unlimited number of arguments, and are placed into the respective placeholders

quantity = 5
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))