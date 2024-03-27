# Slicing = Create a substring by extracting elements from another string
#           indexing[] or slicing()
#           [start:stop:step]

# name = "Hello World"

# first_word = name[0:5] # first_word = name[:5]  [0:5]
# last_word = name[6:11] # last_word = name[6:]  [6:end]
# funky_word = name[0:11:2] # name[::2] [0:end:2]
# reversed_word = name[::-1] # name[0:end:-1]

# print(first_word)
# print(last_word)
# print(funky_word)
# print(reversed_word)

website1 = "https://google.com"
website2 = "https://yahoo.com"
website3 = "https://microsoft.com"

""" Negative  index number counts the characters in reverse starting with -1 
whereas positive index numbers count the characters from 0"""

v_slice = slice(8, -4)
print(website1[v_slice])
print(website2[v_slice])
print(website3[v_slice])
