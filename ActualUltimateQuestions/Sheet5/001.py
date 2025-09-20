# How do you write a function to return the sum of all numbers in a list using a for loop?
"""
n=[1,2,3,4,5]
for i in n:
    print(sum(n))
"""
# What function checks if a list contains an even number using if-else?
"""
l=[1,2,3,4,5]
for i in l:
    if i%2==0:
        print("Even")
    else:
        print("Odd")
"""
# How can you create a function to append a user-entered number to a list if it’s positive?
"""
l=[]
for i in range(5):
    n=int(input("Enter a number:  "))
    if n>0:
        l.append(n)
    else:
        print("Invalid number","Enter a positive number")
print(l)
"""
# What code uses a function to return the maximum value in a list without using max()?
"""
l=[]
for j in range(5):
    x=int(input("Enter a number:  "))
    l.append(x)
n=l[0]
for i in l:
    if i>n:
        n=i
print(n)
"""
# How do you write a function to count how many elements in a list are greater than 10?
l=[]
for i in range(5):
    x=int(input("Enter a number:  "))
    l.append(x)
for j in l:
    if j%2==0:
        print("Even")
    else:
        print("Odd")
print(j.count())
# What function reverses a list using a loop and returns it?

# How can you use if-else to remove all odd numbers from a list in a function?

# What function takes a list and returns a new list with each element doubled?

# How do you write a function to check if a list is empty using if-else?

# What code uses a function to find the index of a user-entered number in a list?
