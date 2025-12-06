# What function returns a list of all keys in a dictionary?
"""
def lis(a):
    result=[]
    for i in a.keys():
        result.append(i)
    return result
print(lis({"Name":"Govind",
           "Grade":"Seven",
           "Section":"A",
           "Age":"Tweleve"}))
"""
# How can you use if-else in a function to update a dictionary value if it’s negative?
"""
def negative(a,b):
    result=a[b]
    if result<0:
        a[b]=0
    else:
        print("Number is safe" )
    print(a)
balances={
    "Marks1":150,
    "Marks2":-50
}
negative(balances,"Marks1")
negative(balances,"Marks2")
print(f"Updated Dictionary:{balances}")
"""
# What function merges two dictionaries and returns the result?
"""
def merge(a,b):
    result=a|b
    return result
print(merge({"Name":"Govind","Age":12},{"Grade":7,"Section":"A"}))
"""
# How do you write a function to remove a user-entered key from a dictionary?
"""
def delete(a,b):
    a.pop(b)
    result=a
    print(result)
delete({"Name":"Govind","Age":12,"Marks":67},"Marks")
"""
# What code uses a function to find the key with the maximum value in a dictionary?
"""
def maximum(a):
    print(max(a.keys()))
maximum({1:2,3:4,5:6,7:8,9:10})
"""
# How can you create a function to return a dictionary with squared values?
"""
def squares(a):
    result=[]
    for i in a.values():
        result.append(i**2)
    return result
print(squares({
    "Grade":6,
    "Age":12,
    "Code":7081,
    "LaMelo Ball":67
}))
"""
# What function checks if all values in a dictionary are strings using if-else?
"""
def string(a):
    result=[]
    for i in a.values():
        if i==str(i):
            result.append(i)
    return len(result)  
print(string({"Name":"Govind","Age":12,"Marks":67,"Hobby":"Basketball"}))
""" 
# How do you write a function to count the number of key-value pairs in a dictionary?
"""
def count(a):
    result=len(a)
    return result
print(count({"Name":"Govind","Age":12,"Marks":67}))
"""
# What code uses a function to return a dictionary with keys swapped with values (if values are unique)?
"""

"""
# How can you use a function to filter a dictionary to include only keys with even values?
"""
def even(a):
    result={}
    for i,j in a.items():
        if j%2==0:
            result[i]=j
    print(result)
even({"a":1,"b":2,"c":3,"d":4})
"""
