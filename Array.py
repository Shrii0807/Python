#Arrays are used to store multiple values in one single variable

#append() method in array
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

print(fruits)
#clear() method in array
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
print(fruits)

#copy() method in array
fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)

#count() method
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

print(x)

#extend() method
fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

print(fruits)

#index() method
fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)

print(x)

#insert() method
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)

