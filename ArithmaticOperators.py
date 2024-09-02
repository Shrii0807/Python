friends = 5
#agumented assignment
friends +=1

print(friends)

friends -=2

print(friends)

friends *=3

print(friends)

friends /=2

print(friends)

friends **=2

print(friends)

remainder = friends % 3
print(remainder)


x=3.14
y=4
z=5
#round function
result = round(x)
print(result)
#abs function
result1 = abs(y)
print(result1)
#pow function
result2= pow(4,3)
print(result2)
#max min  function

result3=max(x,y,z)
result4=min(x,y,z)
print(result3)
print(result4)

#math funcitons
import math

print(math.pi)
print(math.e)
x=9
result= math.sqrt(x)

print(result)

y=9.1
result1 = math.ceil(y)
print(result1)

z= 9.9
result2 = math.floor(z)
print(result2)
#circumference of the circle
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)} cm")


#Area of circle
radius = float(input ("Enter the radius of a circle: "))
area= math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)} cm^2")

# Hypotenus of a triangle
a= float(input("Enter side A: "))
b= float(input("enter side B: "))

c= math.sqrt(pow(a, 2)+ pow(b, 2))

print(f"Side C = {c}")
