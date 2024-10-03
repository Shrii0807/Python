#Python Inheritance
'''Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.'''



class Person(object):
  
  def __init__(self, name, id):
    self.name = name
    self.id = id

  def Display(self):
    print(self.name, self.id)

e = Person("Satyam", 102) 
e.Display()

class Emp(Person):
  
  def Print(self):
    print("Emp class called")
    
Emp_details = Emp("Shrishti", 103)

Emp_details.Display()

Emp_details.Print()
