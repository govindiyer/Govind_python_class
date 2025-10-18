# How do you write a function to return the square of a number?
"""
n=int(input("Enter a number:  "))
def square(n):
    x=n**2
    return x
print(square(n))
"""
# What function returns the sum of two numbers passed as parameters?
"""
def sup(a,b):
    result=a+b
    return result
print(sup(67,83))
"""
# How can a function return the factorial of a given number?
"""
x=int(input("Enter a number:  "))
def factorial():
    factorial=1
    for i in range(1,x+1):
        factorial=factorial*i
    return factorial
n=factorial()
print(n)
"""
# What function returns the maximum of three numbers?
"""
def maximum(a,b,c):
    result=max(a,b,c)
    return result
print(maximum(15,22,42))
"""
# How do you create a function to return the number of vowels in a string?
"""
s=str(input("Enter a word:  "))
def vowel():
    count=0
    for i in s:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            count+=1
    return count
print(vowel())
"""
# What function returns the reverse of a number?
"""

"""
# How can a function return the area of a circle given the radius?
"""
def area(a):
    result=3.14*a*a
    return result
print(area(5))
"""
# What function returns true if a number is even, false otherwise?
"""
def evenodd(a):
    if a%2==0:
        result=(bool(1))
    else:
        result=(bool(0))
    return result
print(evenodd(int(input("Enter a number:  "))))
"""
# How do you write a function to return the sum of digits in a number?
"""
def digitsum(a):
    for i in a:
        print(sum(a))
    return i
print(digitsum([1,2,3,4,5,6,7,8,9]))
"""
# What function returns the length of a string passed as input?
def length(a):
    for i in a:
        result=len(a)
    return result
print(length("Govind"))