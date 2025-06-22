"""

Half Pyramid Pattern
*
* *
* * *
* * * *

"""

n = int(input("Enter the number of rows:"))
print("------------------- Half Pyramid Pattern ------------------")
for i in range(n):
    for j in range(i+1):
        print("* ",end=" ")
    print()

"""

Inverted Half Pyramid Pattern

* * * *
* * *
* *
*
"""
print("--------------------- Inverted Half Pyramid Pattern ------------------")
for i in range(n, 0, -1):
    for j in range(0,i):
        print("* ",end=" ")
    print()


"""

Half Pyramid Pattern
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5

"""
print("--------------------- Half Pyramid Pattern (Numbers)------------------")

for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()

"""

Half Pyramid Pattern
A
B B 
C C C

"""
ascii_value = 65
for i in range(n):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet,end=" ")
    ascii_value +=1
    print()

"""
Floyd's Triangle
1
2 3 
4 5 6 
7 8 9 10

""" 
number = 1
for i in range(n):
    for j in range(i+1):
        print(number,end=" ")
        number+=1
    print()