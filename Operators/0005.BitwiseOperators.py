# Binary Representation -- 

# Binary -- Bi - Two - 1 0 -- 

# 0001 --- 1
# 0010 -- 2 
# 0011  --3
# 0100 - 4
# 0101 - 5
# 0110 --6
# 0111 - 7
# 1000 -- 8
# 1001 -9
# 1010 - 10

"""
0       0       0       0
2^2    2^2     2^1       2^0
4+2
0     1       1         0

14 - 8 + 4+2

24 - 16 + 8 

11000
1110

25 -- 16 + 8 + 1

 5    4   3     2    1    0
      1   1     0    0    1
      
17 --  1 0 0 0 1

"""

# Bitwise Operators :

# & , | , ^ 


#  0 -- 0 
#  1 -- 0 
#  0 -- 1
#  1 -- 1


# 5 - 101 
# 7 - 111
#    1 0 1

# & -- AND
#  0 -- 0 --->  0
#  1 -- 0 ----> 0
#  0 -- 1 --- > 0
#  1 -- 1 ----> 1


#   12 --  1 1 0 0
#   10 --  1 0 1 0
# result = 1 0 0 0
print(5&7)
print(12&10)

# | -- OR 
#  0 -- 0 --->  0
#  1 -- 0 ----> 1
#  0 -- 1 --- > 1
#  1 -- 1 ----> 1


#   12 --  1 1 0 0
#   10 --  1 0 1 0

print(12|10)
# result == 1 1 1 0
# 14 

# 5 - 101 
# 7 - 111
# result = 1 1 1
# 7
print(5|7)

# XOR - Exclusive OR 
#  0 -- 0 --->  0
#  1 -- 0 ----> 1
#  0 -- 1 --- > 1
#  1 -- 1 ----> 0

# 22 - 1 0 1 1 0
# 7 -      1 1 1
# 1 0 0 0 1
print(22^7)


# Left Shift << 
# During left shift we add the extra zeroes on the right side and the left shifted number will alwyas be greater than the original number.

# 22 << 1 
# 1 0 1 1 0 
# 1 0 1 1 0 0 -- This is new number after left shifting 
# 44 --- new number = original number * 2 ^ 1
print(22<<1)
print(22 << 2)
# 22 * 2 ^2  = 88 
# 22 * 2 ^3  = 176
print(22 << 3)

# Right Shift >>
# During right shift we add extra zeroes on the left side and remove the digit from the right side and the right shifted number will alwyas be smaller than the original number

# # 22 >> 2 
# 0 0 1 0 1 

# 0 0 1 0 1 -- This is new number after left shifting 
# 44 --- new number = original number / 2 ^ 2

print(22>>2)
# print(22/4)

print(10>>3)    # 10 / 8 = 1

# Decimal to Binary
# 22  
# 1 0 1 1 0 

# Binary to Decimal 
# 1 0 0 1 0 
#  18 
