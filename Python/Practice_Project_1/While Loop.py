""" While loop is a conditional statement which executes a block of code as long as the given condition is true """

# while 1 == 1:
#    print("Help! I'm stuck in a loop")

# name = ""

# while len(name) == 0:
#    name=input("Enter your name: ")

name = None

while not name:
    name = input("Enter your name: ")
print("Hello " + name)
