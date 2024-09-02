'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

'''
#creating a dictionary
adict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(adict)

#accesing one item in the dictionary
print(adict["brand"])

#String, int, boolean, and list data types in dictionary

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#get keys items() values()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


