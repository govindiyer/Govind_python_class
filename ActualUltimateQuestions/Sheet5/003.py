# What function concatenates two tuples and returns the result?
"""
def concatenate(a,b):
    result=a+b
    return result
print(concatenate((1,2,3,4,5),(6,7,8,9,10)))
"""
# How can you use if-else in a function to check if a tuple contains only positive numbers?
"""
def positive(a):
    for i in a:
        if i<=0:
            return False
    return True
a=(-1,2,3,-4,5,6,-7,8,9,-10)
print(f"{a}:{positive(a)}")
"""
# What function returns a new tuple with elements greater than a user-entered value?
"""
def greater(a,b):
    result=[]
    for i in a:
        if i>b:
            l.append(i)
    return tuple(result)
t=(1,2,3,4,5,6,7,8,9,10)
n=int(input("Enter a number: "))
x=greater(t,n)
print(x)
"""
# How do you write a function to find the minimum value in a tuple using a loop?
"""
def small(a):
    result=min(a)
    return result
print(small((1,2,3,4,5,6,7,8,9,10)))
"""
# What code uses a function to return a tuple’s elements in reverse order?
"""
def reverse(a):
    result=a[::-1]
    return result
print(reverse((10,9,8,7,6,5,4,3,2,1)))
"""
# How do you write a function to add a user-entered number to a set if it’s not already present?
"""
def add(a,b):
    if b not in a:
        result=a.add(b)
    return result
print(add({1,2,3,4,5,6,7,8,9,10}))
my_data_set={10, 20, 30}
print(f"{my_data_set}")
my_data_set.add(40)  
print(f"{my_data_set}")
"""
# What function checks if one set is a subset of another using if-else?
"""
def subs(a,b):
    if a.issubset(b):
        return True
    else:
        return False
print(subs({1,2,3,4,5},{6,7,8,9,10}))
"""
# How can you create a function to return the union of two sets?
"""
def unite(a,b):
    result=a.union(b)
    return result
print(unite({1,2,3,4,5},{6,7,8,9,10}))
"""
# What code uses a function to remove all elements less than 10 from a set?
def delete(a):
    result=[]
    for i in a:
        if i<10:
            result.append(i)
    return set(result)
print(delete({0,2,4,6,8,10,12,14,16,18,20}))
# How do you write a function to find the intersection of two sets?
"""
def inter(a,b):
    result=a.intersection(b)
    return result
print(inter({1,2,3},{1,2,3,9,10}))
"""