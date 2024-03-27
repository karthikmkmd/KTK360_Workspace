""" For Loop executes the block of statements when the given condition is satisfied for a limited amount of times
 whereas while loop will execute unlimited
"""
import time

# for i in range(10):
#    print(i) # index starts with 0

# for i in range(10):
#    print(i+1)

# for i in range(50,100): # outer range is exclusive inner range is inclusive
#     print(i)

# for i in range(50,100+1): # outer range is exclusive inner range is inclusive
#    print(i)

# for i in range(50,100,2): # (start, end, incr)
#    print(i)

# for i in range(50,100+1,2): # (start, end, incr)
#     print(i)

# for i in "Karthik Deivasigamani":
#    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")


