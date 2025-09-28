# What while loop prints numbers from 1 to 100, stopping at 25?
"""
for i in range(1,101):
    if i==26:
        break
    print(i)
"""
# How can you sum numbers from 1 to 30 using a while loop?
"""
n=1
sun=0
while n<=30:
    sun+=n
    n+=1
print(sun)  
"""
# What loop prints numbers divisible by 7 from 7 to 70?
"""
for i in range(7,71):
    # print(i)
    if i%7==0:
        print(i)
"""
# How do you print a user-entered word until a counter reaches 5?
"""
w=str(input("Enter a word:  "))
n=1
while n<=5:
    print(w)
    n+=1
"""
# What code keeps asking for input until a positive number is entered?
"""
n=int(input("Enter a number:  "))
for i in range(n):
    if i>0:
        print("Positive")
        break
"""
# How can you print numbers from 50 to 10 in steps of 2?
"""
for i in range(10,51,2):
    print(i)
"""
# What while loop counts how many times a number can be divided by 2?
"""

"""
# How do you print numbers from 1 to n, where n is user input?
"""
n=int(input("Enter a number:  "))
for i in range(1,n+1):
    print(i)
"""
# What loop prints a pattern of stars in 4 rows (1 star, 2 stars, etc.)?
"""

"""
# How can you print numbers from 1 to 20 that are not multiples of 3?
for i in range(1,21):
    if i%3!=0:
        print(i)