#Python Arrays
#Python does not have built-in support for Arrays, but Python Lists can be used instead.

#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
#An array is a special variable, which can hold more than one value at a time.

#Access the Elements of an Array
#You refer to an array element by referring to the index number.

x = cars[0]
print(x)

#Change the values
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

#The Length of an Array
#Use the len() method to return the length of an array (the number of elements in an array).
cars =  ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)
#Looping Array Elements
for x in cars:
    print(x)

#Adding Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.append("honda")
print(cars)

#Removing Array Elements
#You can use the pop() method to remove an element from the array.
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)