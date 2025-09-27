# How do you print a user-entered number 10 times?
"""
n=int(input("Enter a number:  "))
for i in range(10):
    print(n)
"""
# What for loop prints characters of a string one per line?
"""
w=str(input("Enter a word:  "))
for i in w:
    print(i)
"""
# How can you count numbers from 1 to n, where n is user input?
"""
n=int(input("Enter a number:  "))
for i in range(1,n+1):
    print(i)
"""
# What loop prints numbers from 1 to 100 that are not divisible by 3?
"""
for i in range(1,100+1):
    if i%3!=1:
        print(i)
"""
# How do you print the first 10 Fibonacci numbers using a for loop?
"""
x=0
y=1
for i in range(10):
    n=x+y
    print(n)
    x=y
    y=n
"""
# What code prints a pattern of stars in 5 rows (1 star, 2 stars, etc.)?
"""

"""
# How can you print a multiplication table for 7?
"""
for i in range(1,11):
    print(f"{7} multiplied with {i} is {7*i}")
"""
# What loop sums numbers from 1 to 50?
"""
n=0
for i in range(1,51):
    n+=i
print(f"Total sum = {n}")
"""
# How do you print numbers from n to 1, where n is user input?
"""
n=int(input("Enter a number:  "))
for i in range(n,0,-1):
    print(i)
"""
# What for loop prints every second number from 10 to 20?
for i in range(10,21,2):
    print(i)