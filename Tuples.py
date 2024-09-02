#TUPLE
'''
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
'''
#initialising a basic tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#printing the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1, type(tuple1))

#Access Tuple
#Range of Tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-1])
print(thistuple[-4:-1])

#Check if the item exists in the tuple or not
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Updating tuple (Change tuple value)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#convert tuple into list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#adding tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#remove item from tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#loop tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#Tuple methods 
#There are two built-in tuple methods
'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''

#count tuple
# Creating tuples  
T1 = (0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)  
T2 = ('python', 'java', 'python', 'Tpoint', 'python', 'java')  
# counting the appearance of 3  
res = T1.count(2)  
print('Count of 2 in T1 is:', res)  
# counting the appearance of java  
res = T2.count('java')  
print('Count of Java in T2 is:', res)  

#index method  
Tuple_data = (0, 1, 2, 3, 2, 3, 1, 3, 2)  
# getting the index of 3  
res = Tuple_data.index(3)  
print('First occurrence of 1 is', res)  
# getting the index of 3 after 4th  
# index  
res = Tuple_data.index(3, 4)  
print('First occurrence of 1 after 4th index is:', res)  

