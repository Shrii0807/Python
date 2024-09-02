#logical Operators = evaluate multiple conditions (or, and, not)
#       or = at least one condition must be true
#       and = both conditions must be true
#       not = inverts the condition (not False, not True)

temp = 20
is_raining = str(input("Enter the value if the it is raining or not (True or False): "))

if temp > 35 or temp < 0 or is_raining == "True":
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

#AND operator
temp= 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is Hot outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is Cold outside ☁️")
    print("It is dweey ☀☁️")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm Outside")

#and not
temp= 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is Hot outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is Cold outside ☁️")
    print("It is dweey ☀☁️")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm Outside")
elif temp >= 28 and not is_sunny:
    print("It is Hot outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and not is_sunny:
    print("It is Cold outside ☁️")
    print("It is dweey ☀☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm Outside")