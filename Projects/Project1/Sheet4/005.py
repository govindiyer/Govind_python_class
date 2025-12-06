# How can a function return the product of two numbers?
"""
def product(a,b):
    result=a*b
    return result
print(product(5,10))
"""
# What function returns true if a number is prime?
"""
def prime(a):
    for i in range(1,a):
        if 0:
            result=(bool(1))
        else:
            result=(bool(0))
    return result
print(prime(15))
"""
# How do you write a function to return the Celsius to Fahrenheit conversion?
"""
def celsius(a):
    farenheight=a*1.8+32
    return farenheight
print(celsius(int(input("Enter a number:  "))))
"""
# What function returns the count of characters in a string excluding spaces?
"""
def characters(a):
    count=0
    for i in a:
        count+=1
    return count
print(characters(input("Enter a word:  ")))
"""
# How can a function return the average of a list of numbers?
"""
def avg(li):
    res=0
    for i in li:
        res+=i
    average=res/len(i)
    return average
print(avg([1,2,3,4,5,6,7,8,9]))
""" 
# How do you write a recursive function to calculate the factorial of a number?
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num=5
result=factorial(num)
print(f"The factorial of {num} is {result}") 
"""
# What recursive function returns the nth Fibonacci number?
"""
def fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))
"""
# How can a recursive function print numbers from n to 1?
"""
def reverseorder(n):
  if n < 1:
    return
  print(n)
  reverseorder(n - 1)
reverseorder(int(input("Enter a number:  "))) 
"""
# What recursive function calculates the sum of numbers from 1 to n?
"""
def Sum(n):
    if n <= 1:
        return n
    else:
        return n+Sum(n-1)
n=int(input("Enter a number:  "))
result=Sum(n)
print(f"The sum of numbers from 1 to {n} is: {result}")
"""
# How do you write a recursive function to reverse a string?
"""
def reverse(str):
    if len(str)==0:
        return str
    return reverse(str[1:])+str[0]
if __name__=="__main__":
    str=input("Enter a word:  ")
    print(reverse(str))
"""