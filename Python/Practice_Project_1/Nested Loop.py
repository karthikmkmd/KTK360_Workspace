""" Nested Loops are basically one loop inside another loop. It can be for loop or while loop or combination of both.
when we run the inner loop for n iterations for 1 iteration of the outer loop"""

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")

for i in range(rows):
   for j in range(columns):
       print(symbol, end="") # end = "" will avoid the new line character being inserted after every iteration of inner loop
   print() # introduces new line character


for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()

""" Please refer to the below link for more pyramid patterns with explanation
https://www.programiz.com/python-programming/examples/pyramid-patterns 
https://www.programiz.com/python-programming/examples """
# Example 2: Program to print half pyramid a using numbers
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

#Example 3: Program to print half pyramid using alphabets
#rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")

    ascii_value += 1
    print()

# Programs to print inverted half pyramid using * and numbers
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")

    print()

# Example 5: Inverted half pyramid using numbers
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Example 6: Program to print full pyramid using *
k = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print("* ", end="")
        k += 1

    k = 0
    print()

