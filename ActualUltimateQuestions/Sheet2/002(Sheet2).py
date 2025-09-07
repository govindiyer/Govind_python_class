# How can you check if a number is positive or negative (user input)?
"""
n=int(input("Enter a number:  "))
if n>0:
    print("Positive")
elif n==0:
    print("Neutral")
else:
    print("Negative")
"""
# What program determines if a person can vote (age >= 18, user input)?
"""
n=int(input("Enter a number:  "))
if n>=18:
    print("The person can vote")
else:
    print("The person can't vote")
"""
# How do you check if a number is even or odd (user input)?
"""
n=int(input("Enter a number:  "))
if n%2==0:
    print("The number",n,"is even")
else:
    print("The number",n,"is odd")
"""
# What program finds the larger of two numbers (user input)?
"""
n=int(input("Enter a number:  "))
n1=int(input("Enter another number:  "))
if n1>n:
    print(f"The number {n} is smaller than {n1}")
elif n>n1:
    print(f"The number {n} is greater than {n1}")
else:
    print(f"The number {n} is equal to {n1}")
"""
# How can you check if a year is a leap year (divisible by 4, user input)?
"""
n=int(input("Enter a year of your choice:  "))
if n%4==0:
    print(f"The year {n} is a leap year")
else:
    print(f"The year {n} is not a leap year")
"""
# What program assigns a grade (A, B, C, etc.) based on a score (user input)?
"""
n=int(input("Enter a number:  "))
if n>100:
    print(f"The number {n} is a invalid number")
elif n>90 and n<=100:
    print("A")
elif n>80 and n<=90:
    print("B")
elif n>70 and n<=80:
    print("C")
elif n>60 and n<=70:
    print("D")
elif n>50 and n<=60:
    print("E")
else:
    print("F")
"""    
# How do you check if a number is between 1 and 100 (user input)?
"""
n=int(input("Enter a number:  "))
if n>=1 and n<=100:
    print(f"The number {n} is between 1 and 100")
"""
# What program determines if a character is a vowel or consonant (user input)?
"""
n=input("Enter a letter:  ")
if n=="a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U":
    print(f"The letter {n} is a vowel")
else:
    print(f"The letter {n} is a consonant")
"""
# How can you check if a number is divisible by both 2 and 3 (user input)?
"""
n=int(input("Enter a number:  "))
if n%2==0 and n%3==0:
    print(f"The number {n} is divisible by 2 and 3")
else:
    print(f"The number {n} is not divisible by 2 and 3")
"""
# What program prints 'Hot' if temperature > 30, 'Cold' if < 10, else 'Moderate' (user input)?
"""
n=int(input("Enter a number:  "))
if n>=30:
    print("Hot")
elif n<=10:
    print("Cold")
else:
    print("Moderate")
"""