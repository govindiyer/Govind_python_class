# What function returns the number of elements in a set using len()?
"""
def length(a):
    result=len(a)
    return result
print(length({1,2,3,4,5,6,7,8,9,10}))
"""
# How can you use if-else in a function to check if a set is empty?
"""
def empty(a):
    if len(a)==0:
        return True
    else:
        return False
print(empty({1,2,3,4,5,6,7,8,9,10}))
"""
# What function returns a set of common elements between two lists?
"""
def common(a,b):
    result=a.issubset(b)
    return result
print(common({1,2,3,4,5},{1,2,3,4,5,6,7,8,9,10}))
"""
# How do you write a function to check if a user-entered number exists in a set?
"""
def exist(a,b):
    if b in a:
        return True
    else:
        return False
print(exist({1,2,3,4,5,6,7,8,9,10},int(input("Enter a number:  "))))
"""
# What code uses a function to return the difference between two sets?
"""
def subtract(a,b):
    result=set()
    for i in a:
        if i not in b:
            result.add(i)
    return result
print(subtract({1,2,3,4,5,6,7,8,9,10,11,12,13},{10,9,8,11,12,13,14,15,16,17,18,19,20}))
"""
# How do you write a function to return the value of a user-entered key in a dictionary?
"""
def value(a,b):
    if b in a:
        return a[b]
    else:
        return False
print(value({"Hello":"World","Ok":"Bye"},"Ok"))
"""
# What function checks if a key exists in a dictionary using if-else?
"""
def exist(a,b):
    if b in a:
        return True
    else:
        return False
print(exist({"ABC":123,"DEF":456,"GHI":789,"JKL":101112},"GHI"))
"""
# How can you create a function to add a key-value pair to a dictionary if the key doesn’t exist?
"""
def add(a,b,c):
    if b not in a:
        result=a[b]=c
        return result
    else:
        print(f"{b} already exists. No change made.")
scores = {"Alice":100,'Bob':85}
print(f"Original: {scores}\n")
add(scores,"Charlie",92)
add(scores, "Alice",50)
print(scores)
"""
# What code uses a function to return the sum of all values in a dictionary?
"""
def allsum(a):
    result=sum(a.values())
    return result
print(allsum({"Age":12,"Marks1":98,"Marks2":96,"Marks3":100})) 
"""
# How do you write a function to count how many values in a dictionary are greater than 50?
"""
def count(a):
    result=0
    for i in a.values():
        if i>=50:
            result+=1
    return result
print(count({"Age":12,"Marks1":49,"Marks2":99,"Marks3":100}))
"""