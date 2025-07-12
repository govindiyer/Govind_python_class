# Find count of digits in number

# 12345 -- 5 
# 237890 -- 6 

# Int to string -- len()

# num = 12345
# print(len(str(num)))


# num = 12345
# if num >=0:
#     num-=1
    # 12344
# 12345 -- 5 
# print(12345//10)
# print(12345%10)
# 1234  -- 4 
# 123 -- 3 
# 12 --2 
# 1 -- 1

"""
def CountDigit(n):
    result = 0
    while n !=0:
        n=  n//10
        result+=1
    return result
    
num = 12345
result = CountDigit(num)
print(result)

"""

# SumOfDigits of a Number -- 234 --  9 , 12345 - 15 
"""
def SumOfDigits(n):
    result =0
    while n !=0:
        temp = n%10
        result += temp
        n//=10
    return result

num = 12345
result = SumOfDigits(num)
print(result)

"""

# 12345 %10 --- 5  result = 5  n= 1234
# 1234 %10 -- 4    Result = 9  n = 123
# 123 %10  -- 3    result = 12  n = 12
# 12 %10 -- 2      result = 14   n = 1
# 1 %10 -- 1       result = 15   n = 0 


# Find the Product of the digits of Number :
"""
def DigitProd(n):
    result = 1

    while n !=0:
        temp = n%10
        result *= temp
        n = n //10
    return result

n = 1234
print(DigitProd(n))

"""

# Find the count of Even and Odd Digits in a number 

def CountEvenOdd(n):
    EvenCount = 0
    OddCount = 0

    while n !=0:
        temp = n %10
        if temp %2 ==0:
            EvenCount+=1
        else:
            OddCount+=1
        
        n //= 10
    
    print("Even Count:",EvenCount , " ----------- Odd Count:" , OddCount)

n = 12934556878

CountEvenOdd(n)


"""
Next Questions :

1. Find the largest digit in a number.
2. Count the freq of a sepecific number 
3. Count the Factors of a number
4. Count the Prime and Composite Numbers 
5. Digits greater than a specific number 
6. Count the freq of each and every Digit 
7. Average of the sum of digits of a number 
8. Count multiples of a number 

"""