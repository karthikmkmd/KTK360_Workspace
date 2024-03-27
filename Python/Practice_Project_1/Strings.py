# String manipulation

name = "Karthik Deivasigmani"


print(name) # prints Value of the variable
print(len(name)) # prints Length of the variable

# find function
print(name.find("i"))
print(name.find("i",6,len(name)))
print(name.find("k",0,len(name)))
print(name.find("K",6,len(name)))
print(name.find("K",0,len(name)))

print(name.capitalize()) # Capitalizes only the first character of the word in a sentence
name1 = "this is my hometown. i stay here."
print(name1.capitalize())

print(name.lower()) # Changes content to Lower Case
print(name.upper()) # Changes content to Upper Case

print(name.isdigit()) # checks where the word contains numbers or not
print(name.isalpha()) # checks where the word contains numbers or not

name2 =  "KarthikDeivasigmani"
print(name2.isalpha()) # checks where the word contains alphabets
name3 = "123456789"
print(name3.isdigit()) # checks where the word contains numbers or not
name = "123456478449AB4C"
print(name.isdigit()) # checks where the word contains numbers or not
print(name.isalpha()) # checks where the word contains alphabets
print(name.isalnum()) # checks where the word contains numbers and alphabets
print(name.count("4",0,len(name))) # Counts the occurrences of the character/word

name1 = "this is my hometown. Hyderabad is my workplace."
print(name1.count("is",0,len(name1))) # Counts the occurrences of the character/word
print(name1.replace("o","a"))    # Replaces the given word with new word
print(name1.replace("is","are")) # Replaces the given word with new word

print(name*3) # repeats the word number of times mentioned after *



