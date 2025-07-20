# create a set 
mySet = set()

mySet = {1,2,3,4,5,5,5,5}

# to check if a value exists in the set or not 
# if 41 in mySet:
#     print("4 is present")
# else:
#     print("Not found")

# mySet.add()
# mySet.remove() , mySet.discard()

# mySet.clear()

# union() , intersection()
# len(mySet)

# Find if there are duplicate numbers in the list
# myList = [1,2,3,4,5,4,3,6]
# n = len(myList)
# First Method --- 1 
# False -- No Duplicates , true - There are duplicates 
# print(len(myList)!=len(set(myList)))

# if len(myList) !=len(set(myList)):
#     print("True")
# else:
#     print("False - NO duplicates")

# Second Approach --2 
"""
def find_duplicates(myList):
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i]==myList[j]:
                return True 
    return False

print(find_duplicates(myList))
"""
# Third Approach -- Set()
"""
def find_duplicates(myList):
    seen = set()

    for elem in myList:
        if elem in seen:
            return True 
    
        seen.add(elem)
    return False

print(find_duplicates(myList))
"""

# Count the duplicate number -- [1,2,3,4,5]  return - 0  [1,2,3,4,4,5,5,2] -- return 3 
"""
myList = [1,2,3,4,5,4,3,6]
def CountDuplicates(myList):
    seen= set()
    count =0

    for num in myList:
        if num in seen:
            count+=1
        else:
            seen.add(num)
    
    return count

print(CountDuplicates(myList))
"""

# How to count the unique values
"""
myList = [1,2,3,4,5,4,3,6]
def UniquesValues(myList):
    seen = set()
    count = 0

    for num in myList:
        if num not in seen:
            seen.add(num)
            count+=1
        else:
            continue

    return count 
print(UniquesValues(myList))
"""


# Return only unique even numbers 
# Count number of even and odd (unique)
# Find how many different elements in two lists --
# Give the list of numbers (unique) which are there 
# Find if all the characters in a string are different 

# Find if all the digits in a number are diffrent 

# 
