# How do you write a program to compare two user-entered numbers and print which is larger using relational operators?
"""
n=int(input("Enter a number:  "))
n1=int(input("Enter another number:  "))
if n>n1:
    print(f"The number {n} is greater than the number {n1}")
else:
    print(f"The number {n1} is greater than the number {n}")
"""
# What program checks if a user-entered age is not equal to 18 and greater than 15?
"""
n=int(input("Enter a number:  "))
if n>15 and n!=18:
    print(f"The number {n} is greater than 15 and not equal to 18")
"""
# How can you use relational operators to verify if a list’s length is less than or equal to 10?
"""
n=[1,2,3,4,5,6,7]
if len(n)<=10:
    print(f"The list {n} is smaller than or is equal to 10")
else:
    print(f"The length of the list {n} is greater than 10")
"""
# What program determines if a user-entered tuple’s first element is greater than its last element?
"""
for i in range(5):
    n=int(input("Enter a number:  "))
if n[0]>n[4]:
    print(f"The element {n[0]} is greater than the element {n[4]}")
else:
    print(f"The element {n[0]} is smaller than the element {n[4]}")
"""
# How do you check if a set’s size is strictly less than a user-entered number using relational operators?
"""
s={1,2,3,4,5,6,7,8,9,0}
n=int(input("Enter a number:  "))
if len(s)<n:
    print(f"The set {s} is smaller than the number {n}")
else:
    print(f"The set {s} is greater than the number {n}")
"""
# How do you write a program to simulate a switch-case to assign a day name (e.g., Monday) to a user-entered number (1–7)?
"""
n=int(input("Enter a number:  "))
if n==1:
    print(f"The number {n} is monday")
elif n==2:
    print(f"The number {n} is tuesday")
elif n==3:
    print(f"The number {n} is wednesday")
elif n==4:
    print(f"The number {n} is thursday")
elif n==5:
    print(f"The number {n} is friday")
elif n==6:
    print(f"The number {n} is saturday")
elif n==7:
    print(f"The number {n} is sunday")
else:
    print(f"The number {n} is an invalid number, Try another number between 1 and 7")
"""
# What program uses if-elif-else to categorize a user-entered score into "Low" (<50), "Medium" (50–75), or "High" (>75)?
"""
n=int(input("Enter a number:  "))
if n>75 and n<=100:
    print(f"The number {n} is considered high as the number is greater than 75 and is smaller or equal to 100")
elif n<=75 and n>50:
    print(f"The number {n} is considered medium as the number is smaller or equal to 75 and is greater than 50")
elif n<50 and n>=0:
    print(f"The number {n} is considered low as the number is greater or equal to 0 and is smaller than 50")
else:
    print(f"The number {n} is cosidered an invalid number as the number is  smaller than 0 or it is greater than 100") 
"""     
# How can you simulate a switch-case to map a user-entered month number (1–12) to its name using if-elif-else?
"""
n=int(input("Enter a number:  "))
if n==1:
    print("January")
elif n==2:
    print("febuary")
elif n==3:
    print("march")
elif n==4:
    print("april")
elif n==5:
    print("may")
elif n==6:
    print("june")
elif n==7:
    print("july")  
elif n==8:
    print("august")
elif n==9:
    print("september")
elif n==10:
    print("october")
elif n==11:
    print("november")
elif n==12:
    print("december")
"""
# What program uses if-elif-else to check a user-entered character and prints "Uppercase", "Lowercase", "Digit", or "Special"?
"""
n=input("Enter a character:  ")
if n>="A" and n<="Z":
    print("UPPER CASE")
elif n>="a" and n<="z":
    print("lower case")
elif n>="0" and n<="99":
    print("number")
else:
    print("special")
"""
# How do you write a program to use if-elif-else to determine a discount (10%, 20%, 30%) based on a user-entered purchase amount?
"""
n=int(input("Enter a number:  "))
if n<=1000:
    print("You get 10% discount")
    print("The cost of a item you purchased which is below 1000 is now reduced by 10 percent")
    print("Final bill:",n-10/100*n)
elif n>1000 and n<=1500:
    print("You get 20% discount")
    print("The cost of a item you purchased which is above 1000 and below 1500 is now reduced by 20 percent")
    print("Final bill:",n-20/100*n)
    
else:
    print("You get 30% discount")
    print("The cost of a item you purchased which is greater than 1500 is now reduced by 30 percent")
    print("Final bill:",n-30/100*n)
"""