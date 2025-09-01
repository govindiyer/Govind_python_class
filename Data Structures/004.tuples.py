# Lists , Dictionary , Sets 

# tuples - immutable -- We can't add or remove elements froma tuple 

# Ordered Collection , index 

tuple1 = tuple()
print(tuple1)

tuple2 = (42,)
tuple3 = (34)
print(tuple2)
print(type(tuple2))
print(tuple3)
print(type(tuple3))

tuple4 = (23,34,56,74,21,34)
print(tuple4)
print(len(tuple4))

# min -- to find the minimum elements present in the tuple
print(min(tuple4))

# max - to find the largest element in the tuple

print(max(tuple4))

# sum -- to find the sum of all the elements of the tuple 

print(sum(tuple4))


# sorted -- to sort the tuple in increasing order 

print(sorted(tuple4))

# tuple is an index based data structure
# (23,  34, 56, 74, 21, 34)
#  0    1   2   3   4    5  
# -6   -5  -4. -3  -2   -1 
print(tuple4[4])

print(tuple4[-1])
print(tuple4[-4])

# Slicing -  

# tuple4[start:end] -- Start should always be smaller than end -- Start is included but end is excluded

print(tuple4[2:5])

# Slicing with negative indexing

print(tuple4[-5:-1])
print(tuple4[-1:-5])

# del tuple4
# print(tuple4)

# Clear() method does not work with tuple 
# print(tuple4.clear())

# If we want to make changes to the tuple we have to convert it into another data structures 

tuple5 = (12,34,56,78,90)
print(tuple5)
list1 = list(tuple5)
list1.append(11345)
tuple5 = tuple(list1)
print(tuple5)

print(tuple5+ tuple2)



# Unpacking the tuple
print("------------- Unpacking Tuples ----------------- ")
cars = ("BMW","AUDI","Fortuner","Range Rover","Nano")

# a,b,c ,d ,e = cars 
# print(e)

# First and Last Value 
# a , *b ,e = cars 
# print(a,b,e)


