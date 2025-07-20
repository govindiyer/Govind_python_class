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


n=int(input("Enter a number"))
i=0
while n>0:
    j=n%10
    if i<j:
        max=j
    num=num//10
print("The maximum digit in the number is,",i)