# How do you write a function that uses the append() method to add a user-entered number to a list if it’s greater than 0?
"""
def add(a,b):
    if b>0:
        a.append(b)
    print(a)
add([1,2,3,4,5,6,7,8,9],int(input("Enter a number:  ")))
"""
# What function uses the pop() method to remove the last element of a list and returns the updated list if it’s not empty?
"""
def delete(a):
    a.pop()
    if len(a)>0:
        print(a)
delete([1,2,3,4,5,6,7,8,9,10,11])
"""
# How can you create a function that uses the sort() method to sort a list in ascending order and checks if the list has more than 3 elements?
"""
def ascend(a):
    a.sort()
    if len(a)>3:
        print(a)
    else:
        print("List is too small,could add some more elements")
ascend([10,9,8,7,6,5,4,3,2,1])
"""
# What code uses the count() method in a function to return how many times a user-entered value appears in a list?
"""
def count1(a,b):
    result=a.count(b)
    return result
print(count1([1,2,3,4,5,6,7,8,9,10],5))
"""
# How do you write a function that uses the extend() method to combine two lists and returns the result if the combined length is greater than 5?
"""
def combine(a,b):
    a.extend(b)
    print(a)
    if len(a)>5:
        print(f"The list has more than 5 elements")
combine([1,2,3,4,5],[6,7,8,9,10])
"""
# How do you write a function that uses the index() method to find the position of a user-entered number in a tuple, returning -1 if not found?

# What function uses the count() method to check if a tuple has more than two occurrences of 0 and returns True or False?
"""
def countof0(a):
    result=a.count(0)
    return result
print(countof0((0,1,2,3,4,5,6,7,8,9,10)))
"""
# How can you create a function that uses the len() method to return a tuple’s length and prints “Long” if it’s greater than 4?
"""
def length(a):
    if len(a)>4:
        print("Long")
    else:
        print("Short")
length((1,2,3,4,5,6,7,8,9,10))
"""
# How do you write a function that uses the add() method to insert a user-entered number into a set and returns the updated set?
"""
def adding(a,b):
    a.add(b)
    print(a)
adding({1,2,3,4,5,6,7,8,9},10)
"""
# What function uses the discard() method to remove a user-entered element from a set if it exists and returns the set?
"""
def delete(a,b):
    if b in a:
        a.discard(b)
    else:
        print("none")
    print(a)
delete({1,2,3,4,5,6,7,8,9,10},int(input("Enter a number:  ")))
"""