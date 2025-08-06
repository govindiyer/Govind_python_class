# Tuple -- 

myTuple = (20,30)

# x = (30)
# x = 40 

print(type(myTuple))
# print(type(x))


# List , Tuple , Sets , Dictionary 

# list -- Mutable , Indexed based , Duplicate values can be added , Ordered , 
# myList = [1,2,3,65,54,32]

# Tuples - immutable , indexed based , duplicates , ordered 

# Sets -- mutable , not indexed based , no duplicates , unordered

# Dictionary -- Key value pair , mutable , duplicates are allowed (only values should be duplicates),ordered


# Slicing 

myTuples = (12,34,56,78,56,78)
myList = [1,2,3,65,54,32]

# print(myList[2:5])

# print(myTuples[2:5])

# How to add an element to a tuple 

# myTuples[5]=100

# list() , set() , tuple , dict()

# newList = list(myTuples)
# .
# . DO the operations
# .
# .

# myTuples = tuple(newList)

# Upacking of tuples 

cars = ("BMW","AUDI","SKODA","Range Rover","Land Rover")

# (a, b, c , d ,e ) = cars
# print(a,b,c,d,e)

(a, *rest,e ) = cars
print(a,e)




