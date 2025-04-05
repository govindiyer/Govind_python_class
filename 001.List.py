# List -- A data type in Python 

# int float string bool 
x = 10
x = 30

List = [1,2,3,4,56,6,7,1000,1000,"Hello",True,34.56,3456, "SayHello",False,1000]
# print(List)
# How do we access any element of the list ?

#. indexed data structure 

# [11, 24, 35, 46, 56, 96, 7,"Hello",True,34.56]
#   0  1   2   3    4   5  6   7       8     9 
# -10  -9 -8 -7     -5  -4.  -3      -2.    -1 

# print(List[0])

# print(List[6])

# print(len(List))

# How to get the last element of the list
print(List[len(List)-1])
print(List[-1])

# Updating an element 
List[5] = 1000
# print(List)

# Appending elements in the lists 
List.append("New Item")
# print(List)

# To append at a specific index
List.insert(4,2456)
# print(List)


# Remove -- 
List2 = [7,1000,1000,"Hello",34.56,3456, "SayHello",1000]
List2.remove(1000)
# print(List2)

List2.pop(5)
List2.pop()
print(List2)

# deleting the list 
# del List
# print(List)


# Clear -- to empty a list 
# List.clear()
# print(List)


# Negative Indexing 
# We can access a particluar element using negative indexing also
# print(List[-5])

# Slicing :

#  [start:end]      -- end is not included -- 3;6 , 3,4 5 --  6 is not included 
# print(len(List))
print(List[3:7])

print(List[:])

print(List[4:])

print(List[:9])


# start value should always be smaller than the end 

print(List[-9:-3])
print(List[-3:-9])


# List is dynamic data structure. We can add as many as elements into a list

# List is type independent which means we can add values of different types 

# List is indexed data structure.

# List allows duplicate values 


# We can fiund the number of elements present in a list using len() function

# We can find the type of the list using type() function
print(type(List))


# We can create a list using the list() function also 

# List items are changeable 

# Lists are not ordered by defualt 
