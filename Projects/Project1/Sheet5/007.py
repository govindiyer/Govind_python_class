# How can you create a function that uses the union() method to combine two sets and checks if the result has more than 10 elements?
"""
def join(a,b):
    a.union(b)
    if len(a)>10:
        print(True)
    else:
        print(False)
join({1,2,3,4,5},{6,7,8,9,10})
"""
# What code uses the intersection() method in a function to return common elements between two sets and prints “No overlap” if empty?
"""
def intersect(a,b):
        print(a.intersection(b))
intersect({1,2,3,4,5},{5,6,7,8,9,10})
"""
# How do you write a function that uses the clear() method to empty a set if it has more than 5 elements and returns the set?
"""
def delete(a):
    if len(a)>5:
        a.clear()
    print(a)
delete({1,2,3,4,5,6,7,8,9,10})
"""
# What function uses the difference() method to return elements in one set but not another and checks if the result is non-empty?
"""
def diff(a,b):
    if len(a) and len(b)>0:
        a.difference(b)
    print(a)
diff({1,2,3,4,5},{6,7,8,9,10})
"""
# How do you write a function that uses the get() method to return the value of a user-entered key, defaulting to “Not found” if the key doesn’t exist?
"""
def exist(a,b):
    if b in a:
        result=a.get(b)
    else:
        print("Not found")
    print(result)
exist({"Name":"Govind","Age":"Tweleve","Class":"Seven","Section":"A"},"Name")
"""
# What function uses the pop() method to remove a user-entered key from a dictionary and returns the removed value or “Key not found”?
"""
def delete(a,b):
    if b in a:
        a.pop(b)
    else:
        print("No KEY exists")
    print(a)
delete({"Name":"Govind","Age":"Tweleve","Class":"Seven","Section":"A"},"Name")
"""
# How can you create a function that uses the keys() method to return a list of dictionary keys and checks if there are more than 3 keys?
"""
def count(a):
    result=list(a.keys())
    if len(result)>3:
        print("There are more than 3 keys")
    else:
        print("There are les than 2 keys")
count({"Name":"Govind","Age":"Tweleve","Class":"Seven","Section":"A"})
"""
# What code uses the valuess() method in a function to sum all values in a dictionary and returns 0 if the dictionary is empty?
"""
def sum1(a):
    if len(a)>0:
        print(sum(a.values()))
    else:
        print("Dictionary is empty")
sum1({"Name":3,"Age":12,"Class":7,"Section":8})
"""
# How do you write a function that uses the update() method to add a new key-value pair to a dictionary if the key doesn’t exist?
"""
def key(a,b):
    if b not in a.keys():
        result=a[b]="Earth"
    else:
        print("Present in the dictionary")
    print(a)
key({"Name":"Govind","Age":"Tweleve","Class":"Seven","Section":"A"},"Planet")
"""
# What function uses the items() method to print all key-value pairs in a dictionary and returns True if all values are positive?
