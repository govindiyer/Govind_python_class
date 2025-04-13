# Sets --

#1 . Sets don't allow duplicate values 

# Hence it is used for storing unique / distinct elements.

mySet= {1,12,3,4,4,-5,4,15,54,-100}
print(len(mySet))
print(mySet)

# 2. These are not index based.
# print(mySet[2])

# Unordered set -- there is not fix output of printing the elements.

# Mutable -- We can add ot remove elements from sets 

# Adding a new element

mySet.add(1000)
print(mySet)

mySet.update([13,24],{345,23456})
print(mySet)


# remove an element
# Remove will throw an error if the element is not present in the set

# mySet.remove(54)
# mySet.remove(154)
print(mySet)


# Discard
# Discard will not throw an error if the element is not present in the set
# mySet.discard(345)
# mySet.discard(154)
# print(mySet)


# Pop removes a random element from the set everytime
# print(mySet.pop())
# print(mySet.pop())

# clear --
# mySet.clear()
# print(mySet)


# del
# del mySet
# print(mySet)

# Copying a set to another 
mySet2= mySet
print(mySet2)

mySet3 = mySet.copy()
print(mySet3)

# Length of the set 
print(len(mySet))


# Union , Intersection , disjoint sets 
mySetA = {12,34,56,78,90,89}
mySetB = {12,23,24,27,89,70}

# Union of two sets -- Combining the sets 
mySetAUnionB= mySetA.union(mySetB)
# mySetAUnionB= mySetA |mySetB
print(mySetAUnionB)

# Displaying only common elements 
mySetAIntersectionB = mySetA.intersection(mySetB)
# mySetAIntersectionB = mySetA & mySetB
print(mySetAIntersectionB)

# Disjoint sets -- Means sets have nothing in common
# Will return true is they have nothing in common else false

print(mySetA.isdisjoint(mySetB))

## Important points about sets 
print(30*"-")
mySet11 ={1,0}
print("mySet11:",mySet11)

mySet12 ={1,0,True}
print("mySet12:",mySet12)

mySet13 ={1,0,True,False}
print("mySet13:",mySet13)

mySet14 ={True,False,1,0}
print("mySet14:",mySet14)

mySet15 ={1,0,1.0,0.0}
print("mySet15:",mySet15)

mySet16 ={1,"1",0,1.0,0.0}
print("mySet16:",mySet16)

mySet17 ={2.00,2,0,1,1,0.0,1.0}
print("mySet17:",mySet17)
