#if = Do some code only if some condition is TRUE
# Else do something else
'''
age= int(input("Enter your age: "))
if age>=100:
    print(" You are too old to sign up!")
elif age<0:
    print("You haven't been born yet!")
elif age>=18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up")

'''

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("there's no food for you")

name= input("Enter your name: ")
if name=="":
    print(" You did not type in your name!")
else:
    print(f"Hello {name}")

online = True
if online:
    print("This item is for sale")
else:
    print("This item is not for sale")


