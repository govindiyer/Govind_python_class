# How can you create a function to merge two lists and return the result?
"""
def merge(a,b):
    result=a+b
    return result
print(merge([1,2,3,4,5],[6,7,8,9,10]))
"""
# What function sorts a list in descending order using a loop (no sort())?
"""
def desending(a):
    result=[]
    for i in range(len(a)-1,-1,-1):
        result.append(a[i])
    return result
print(desending([1,2,3,4,5,6,7,8,9,10]))
"""
# How do you write a function to count duplicates in a list using a loop?
"""
def count(a):
    result=0
    for i in a:
        if i==a[i]:
            result+=1
    return result
print(count([1,2,3,4,5,4,6,7,8,7,9,10,9]))
"""
# What function takes a list and returns only elements divisible by 3?
"""
def divide(a):
    result=[]
    for i in a:
        if i%3==0:
            result.append(i)
    return result
print(divide([1,2,3,4,5,6,7,8,9,12]))
"""
# How can you use a function to replace all negative numbers in a list with 0?
def negative(a):
    result=[]
    for i in range(a):
        if i<0:
            i=0
            result.append(i)
    return result
print(negative[-1,2,-3,4,-5,6,-7,8,-9,10])
# How do you write a function to return the length of a tuple using len()?

# What function checks if a user-entered number exists in a tuple using if-else?

# How can you create a function to return the sum of all elements in a tuple?

# What code uses a function to count how many times 5 appears in a tuple?

# How do you write a function to return the first and last elements of a tuple?
