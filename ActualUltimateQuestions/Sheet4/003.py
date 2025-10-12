# How do you write a function to return the sum of numbers from 1 to 10?
"""
def sumofnum():
    result=0
    for i in range(1,11):
        result+=i
    return result
print(sumofnum())
"""
# What function returns the current time as a string?
"""
import time
def current_time():
    currenttime=time.localtime()
    hour=str(currenttime.tm_hour).zfill(2)
    minute=str(currenttime.tm_min).zfill(2)
    second=str(currenttime.tm_sec).zfill(2)
    return f"{hour}:{minute}:{second}"
current=current_time()
print(current)
"""
# How can a function return the count of even numbers from 1 to 20?
"""
def even():
    for i in range(2,21,2):
        print(i)
even()
"""
# What function returns the product of numbers from 1 to 5?
"""
def product():
    product=1
    for i in range(1,6):
        product=product*i
    return product
n=product()
print(n)
"""
# How do you create a function to return a random number between 1 and 100?
"""
import random
def random_number():
  return random.randint(1, 100)
n=random_number()
print(f"A random number between 1 and 100: {n}")
"""
# What function returns the length of a hardcoded string?
"""
s="Govind"
def length(s):
    result=0
    for i in s:
        result+=1
    return result
print(length(s))
"""
# How can a function return the first Fibonacci number after 10 iterations?
"""

"""
# What function returns the sum of squares from 1 to 5?
"""
l=[1,2,3,4,5]
def squares(l):
    result=0
    for i in l:
        x=i**2
        result+=x
    return result
print(squares(l))
"""
# How do you write a function to return the number of vowels in a fixed string?
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
# What function returns the factorial of 5?
"""
def factorial():
    factorial=1
    for i in range(1,6):
        factorial=factorial*i
    return factorial
n=factorial()
print(n)
"""