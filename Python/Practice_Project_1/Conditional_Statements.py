# if statement = a block of that will execute if it's condition is true

# age = int(input("Enter your age:"))
# """ Order of the if condition matters else the 1st condition that meets if it satisfies it will continue"""
#
# if age == 100:
#     print("You are Century years old!")
# elif age >= 18:
#     print("You are adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# elif age < 18 and age >= 13:
#     print("You are Tean age!")
# else:
#     print("You are a child!")

""" Logical Operators (and, or, not)
    used to check if two or more condition statements is true"""
temp = int(input("Enter the temperature in Celsius: "))

# if temp >=0 and temp <= 30:
#     print("The temperature outside is good today!")
#     print("Go outside Today!")
# elif temp <0 or temp > 30:
#     print("The temperature outside is good today!")
#     print("Go outside Today!")

# Simplified Chain Comparison     for expressions like (a<b) and (b<c) can be written as a<b<c
# if 0 <= temp <= 30:
#     print("The temperature outside is good today!")
#     print("Go outside Today!")
# elif temp < 0 or temp > 30:
#     print("The temperature outside is bad today!")
#     print("Don't go outside Today!")

if not(temp >=0 and temp <= 30):
    print("The temperature outside is bad today!")
    print("Don't go outside Today!")
elif not(temp <0 or temp > 30):
    print("The temperature outside is good today!")
    print("Go outside Today!")

