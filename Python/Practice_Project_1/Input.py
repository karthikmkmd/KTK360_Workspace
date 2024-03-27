name = input("Enter your name: ")
# age = input("Enter your age: ")

print("Hello "+name)
#print("My age is "+age)

# try to add age
# age = age + 1
# print("This is my age "+age) # throws error due to typecast issue str to int

# age = int(age) + 1
# print("This is my age1 "+age) # throws error due to typecast issue int to str
# print("You are "+str(age)+ " years old") # works fine as it has necessary typecast


age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print("You are "+str(age) + " years old") # works fine as it has necessary typecast
print("You are "+str(height) + " cm tall")

