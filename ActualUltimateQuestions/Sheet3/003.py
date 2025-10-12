# How can you print a triangle pattern of numbers (1, 12, 123)?
"""
for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=" ") 
    print()
"""
# What code counts how many numbers from 1 to 100 are divisible by 6?
"""
n=0
for i in range(1,101):
    if i%6==0:
        n+=1
print(n)
"""
# How do you print numbers from 1 to 10 with their cubes?
"""
for i in range(1,11):
    print(f"The cube of {i} is {i**3}")
"""
# What loop prints a reverse pattern of stars (5 stars, 4 stars, etc.)?
"""

"""
# How can you print numbers from 1 to 30 that end with 7?
"""
for i in range(1,31):
    if i%10==7:
        print(i)
"""
# How do you print numbers from 1 to 15 using a while loop?
"""
n=1
while n<=15:
    print(n)
    n+=1
"""
# What while loop counts down from 20 to 1?
"""
n=20
while n>=1:
    print(n)
    n-=1
"""
# How can you print even numbers from 2 to 40 using a while loop?
"""
n=2
while n<=40:
    print(n)
    n+=2
"""
# What code prints odd numbers from 1 to 21?
"""
for i in range(1,22,2):
    print(i)
"""
# How do you print multiples of 5 up to 50?
"""
for i in range(1,11):
    print(f"{5} multiplied with {i} is equal to {5*i}")
"""