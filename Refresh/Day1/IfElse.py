# ============================================================
# PYTHON IF ELSE
# ============================================================

# ============================================================
# QUESTION 1: Electricity Bill Calculator
# ============================================================
#
# Write a program that calculates an electricity bill based
# on the number of units consumed.
#
# Pricing:
#
# 0 to 100 units       -> ₹5 per unit    5*100
# 101 to 200 units     -> ₹7 per unit    7*100
# 201 to 300 units     -> ₹10 per unit   10*50
# Above 300 units      -> ₹15 per unit
#
# If the total bill exceeds ₹2000, add a 5% surcharge.
#
# Example:
#
# Input:
# units = 250
#
# Expected:
# Bill = 2150
#
# Test Cases:
#
# Input: 50
# Expected: 250
#
# Input: 150
# Expected: 850
#
# Input: 250
# Expected: 1650
#
# Input: 400
# Expected: 4400
#
# Input: 500
# Expected: 6050
#
# ------------------------------------------------------------

# Write your solution here
"""
units=int(input("Enter the number of units:  "))
bill=0
if units>=0 and units<=100:
    bill+=units*5
elif units<201:
    bill+=(units-100)*7+units*5
elif units<301:
    bill+=(units-200)*10+100*7+100*5
else:
    bill+=(units-300)*15+100*10+100*7+100*5
print("The electricity fee is Rs.",bill)
if bill>2000:
    print("Due to the high usage of electricity in your house, we are to add 5 percent to your total.")
    extra=0.05*bill
    total_bill=bill+extra
    print("the electricity fee with the 5 percent extra fee is Rs.",total_bill)
"""
# ============================================================
# QUESTION 2: Student Grade Calculator
# ============================================================
#
# Take marks for 5 subjects.
#
# Calculate the percentage and assign a grade:
#
# 90% or above -> A
# 80% to 89%   -> B
# 70% to 79%   -> C
# 60% to 69%   -> D
# 50% to 59%   -> E
# Below 50%    -> F
#
# Additional rule:
#
# If ANY subject has marks below 35,
# the student must be marked as "Fail".
#
# Test Cases:
#
# Input:
# 90
# 90
# 90
# 90
# 90
#
# Expected:
# Percentage: 90
# Grade: A
#
# Input:
# 80
# 85
# 82
# 88
# 85
#
# Expected:
# Percentage: 84
# Grade: B
#
# Input:
# 80
# 80
# 80
# 80
# 30
#
# Expected:
# Fail
#
# Input:
# 55
# 60
# 58
# 62
# 65
#
# Expected:
# Grade: E
#
# ------------------------------------------------------------

# Write your solution here
"""
name=str(input("Enter your name:  "))
english=int(input("Enter your english marks:  "))
csc=int(input("Enter your csc marks:  "))
sst=int(input("Enter your sst marks:  "))
math=int(input("Enter your math marks:  "))
science=int(input("Enter your science marks:  "))
print("The name of the student is",name)
print("Your english marks are",english)
print("Your csc marks are",csc)
print("Your math marks are",math)
print("Your sst marks are",sst)
print("Your science marks are",science)
avg=(english+csc+math+sst+science)/5
print("Your average marks are",avg)
if avg>89:
    print("A")
elif avg>79 and avg<90:
    print("B")
elif avg>69 and avg<80:
    print("C")
elif avg>59 and avg<70:
    print("D")
elif avg>49 and avg<60:
    print("E")
else:
    print("F") 
print("Congratulations, you have moved on to the next grade!!!")
"""
# ============================================================
# QUESTION 3: Login Authentication
# ============================================================
#
# Create a simple login system.
#
# Correct username:
# admin
#
# Correct password:
# admin123
#
# Rules:
#
# Correct username + correct password
# -> Login successful
#
# Correct username + wrong password
# -> Incorrect password
#
# Wrong username
# -> User not found
#
# Special case:
#
# username = admin
# password = admin123
#
# -> Welcome Admin
#
# Test Cases:
#
# Input:
# username = "admin"
# password = "admin123"
#
# Expected:
# Welcome Admin
#
# Input:
# username = "admin"
# password = "hello123"
#
# Expected:
# Incorrect password
#
# Input:
# username = "user"
# password = "admin123"
#
# Expected:
# User not found
#
# ------------------------------------------------------------

# Write your solution here
"""
username=input("Enter the user:  ")
password=input("Enter the password:  ")
if username=="admin" and password!="admin123":
    print("Incorrect password, please try again")
elif username!="admin" and password=="admin123":
    print("Incorrect user, please try again")
elif username!="admin" and password!="admin123":
    print("Incorrect user and password, please try again")
else:
    print("Login verified")
"""
# ============================================================
# QUESTION 4: Triangle Validator
# ============================================================
#
# Take three sides of a triangle.
#
# First check whether the three sides can form a valid
# triangle.
#
# A triangle is valid if:
#
# a + b > c
# b + c > a
# a + c > b
#
# If valid, classify the triangle:
#
# All three sides equal
# -> Equilateral
#
# Any two sides equal
# -> Isosceles
#
# All three sides different
# -> Scalene
#
# Test Cases:
#
# Input:
# 5
# 5
# 5
#
# Expected:
# Equilateral
#
# Input:
# 5
# 5
# 8
#
# Expected:
# Isosceles
#
# Input:
# 4
# 5
# 6
#
# Expected:
# Scalene
#
# Input:
# 1
# 2
# 5
#
# Expected:
# Invalid Triangle
#
# ------------------------------------------------------------

# Write your solution here
"""
side1=int(input("Enter a number:  "))
side2=int(input("Enter a number:  "))
side3=int(input("Enter a number:  "))
if side1+side2>side3 or side3+side2>side1 or side1+side3>side2:
    print("Triangle is valid")
    if side1==side2==side3:
        print("Equilateral triangle")
    elif side1==side2!=side3 or side3==side2!=side1 or side1==side3!=side2:
        print("Isoceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Triangle is invalid")
perimeter=side3+side1+side2
print("Perimeter of the triangle is",perimeter)
"""
# ============================================================
# QUESTION 5: ATM Withdrawal System
# ============================================================
#
# Create an ATM withdrawal program.
#
# Take:
#
# account_balance
# withdraw_amount
#
# Rules:
#
# 1. Withdrawal amount must be greater than 0.
#
# 2. Withdrawal amount must be a multiple of 100.
#
# 3. Withdrawal amount must not exceed account balance.
#
# 4. Minimum balance after withdrawal must be ₹500.
#
# Test Cases:
#
# Input:
# Balance = 10000
# Withdraw = 2000
#
# Expected:
# Withdrawal successful
# Remaining balance = 8000
#
# Input:
# Balance = 10000
# Withdraw = 250
#
# Expected:
# Amount must be a multiple of 100
#
# Input:
# Balance = 10000
# Withdraw = 12000
#
# Expected:
# Insufficient balance
#
# Input:
# Balance = 10000
# Withdraw = 9700
#
# Expected:
# Minimum balance requirement not satisfied
#
# Input:
# Balance = 10000
# Withdraw = -500
#
# Expected:
# Invalid withdrawal amount
#
# ------------------------------------------------------------

# Write your solution here
"""
import sys
account_balance=int(input("Enter your total balance:  "))
withdrawal=int(input("Enter the value you want to withdraw:  "))
remaining=account_balance-withdrawal
if account_balance==0 or withdrawal%100!=0 or withdrawal>account_balance or remaining<500:
    print("Due to some certain rules, we cannot accept your withdrawal")
    sys.exit()
print("Remaining balance,",remaining)
"""
# ============================================================
# QUESTION 6: Movie Ticket Pricing
# ============================================================
#
# Ticket price depends on age:
#
# Below 5        -> Free
# 5 to 12        -> ₹100
# 13 to 59       -> ₹200
# 60 or above    -> ₹120
#
# Wednesday has a 20% discount.
#
# Other days have no discount.
#
# Take age and day as input.
#
# Test Cases:
#
# Input:
# Age = 4
# Day = Monday
#
# Expected:
# Ticket Price = 0
#
# Input:
# Age = 10
# Day = Monday
#
# Expected:
# Ticket Price = 100
#
# Input:
# Age = 30
# Day = Monday
#
# Expected:
# Ticket Price = 200
#
# Input:
# Age = 30
# Day = Wednesday
#
# Expected:
# Ticket Price = 160
#
# Input:
# Age = 65
# Day = Wednesday
#
# Expected:
# Ticket Price = 96
#
# ------------------------------------------------------------

# Write your solution here
"""
age=int(input("Enter your age:  "))
day=int(input("Enter a number from one through seven:  "))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("value invalid")
if age<=5:
    price=0
elif age>5 and age<=12:
    price=100
elif age>12 and age<=60:
    price=200
else:
    price=120
if day==3:
    print("20% discount")
    discount=0.2*price
    price-=discount
print(price)
"""
# ============================================================
# QUESTION 7: Employee Bonus Calculator
# ============================================================
#
# Take:
#
# years_of_service
# salary
# performance_rating
#
# Rules:
#
# Rating >= 9:
#
# Service >= 10 years -> 20% bonus
# Service >= 5 years  -> 15% bonus
# Otherwise            -> 10% bonus
#
# Rating >= 7:
#
# Service >= 5 years  -> 10% bonus
# Otherwise            -> 5% bonus
#
# Rating < 7:
#
# No bonus
#
# Calculate:
#
# Bonus amount
# Final salary
#
# Test Cases:
#
# Input:
# Salary = 50000
# Service = 12
# Rating = 9
#
# Expected:
# Bonus = 10000
# Final Salary = 60000
#
# Input:
# Salary = 50000
# Service = 6
# Rating = 8
#
# Expected:
# Bonus = 5000
# Final Salary = 55000
#
# Input:
# Salary = 50000
# Service = 2
# Rating = 9
#
# Expected:
# Bonus = 5000
# Final Salary = 55000
#
# Input:
# Salary = 50000
# Service = 10
# Rating = 6
#
# Expected:
# Bonus = 0
# Final Salary = 50000
#
# ------------------------------------------------------------

# Write your solution here
"""
salary=int(input("Enter your salary:  "))
years=int(input("Enter your years of service:  "))
rating=float(input("Enter your rating of one through ten:  "))
if rating>=9 and rating<=10:
    if years>=10:
        increase=(0.2)*salary
    elif years>=5 and years<10:
        increase=(0.15)*salary
    else:
        increase=(0.1)*salary
elif rating>=7 and rating<=9:
    if years>=5:
        increase=(0.1)*salary
    else:
        increase=(0.05)*salary   
else:
    increase=(0.0)*salary
salary_increase=salary+increase
print("Your salary is",salary_increase)
"""
# ============================================================
# QUESTION 8: Number Classification
# ============================================================
#
# Take an integer.
#
# First determine:
#
# Positive
# Negative
# Zero
#
# If the number is positive, additionally determine:
#
# Even or Odd
# Divisible by 3 or Not Divisible by 3
#
# Test Cases:
#
# Input: 18
#
# Expected:
# Positive
# Even
# Divisible by 3
#
# Input: 17
#
# Expected:
# Positive
# Odd
# Not Divisible by 3
#
# Input: -10
#
# Expected:
# Negative
#
# Input: 0
#
# Expected:
# Zero
#
# ------------------------------------------------------------

# Write your solution here
"""
number=float(input("Enter a number: "))
if number>0:
    print("Positive")
    if number%2==0:
        print("Even")
        if number%3==0:
            print("Divisible by 3")
        else:
            print("Not divisible by 3")
    else:
        print("Odd")
elif number<0:
    print("Negative")
    if number%2==0:
        print("Even")
        if number%3==0:
            print("Divisible by 3")
        else:
            print("Not divisible by 3")
    else:
        print("Odd")
else:
    print(0)
"""
# ============================================================
# QUESTION 9: Online Shopping Discount
# ============================================================
#
# Take:
#
# cart_amount
# is_member
#
# Discount rules:
#
# Amount >= ₹10,000 -> 20%
# Amount >= ₹5,000  -> 10%
# Amount >= ₹2,000  -> 5%
# Below ₹2,000      -> No discount
#
# Members get an additional 5% discount.
#
# Calculate:
#
# Original Amount
# Discount
# Final Amount
#
# Test Cases:
#
# Input:
# Amount = 1000
# Member = False
#
# Expected:
# Discount = 0
# Final Amount = 1000
#
# Input:
# Amount = 3000
# Member = False
#
# Expected:
# Discount = 150
# Final Amount = 2850
#
# Input:
# Amount = 6000
# Member = False
#
# Expected:
# Discount = 600
# Final Amount = 5400
#
# Input:
# Amount = 10000
# Member = True
#
# Expected:
# Discount = 2500
# Final Amount = 7500
#
# ------------------------------------------------------------

# Write your solution here
"""
amount=float(input("Enter a number:  "))
member=float(input("Enter a number:  "))
if amount>=10000:
    discount=0.2*amount
elif amount>=5000 and amount<10000:
    discount=0.1*amount
elif amount>=2000 and amount<5000:
    discount=0.05*amount
else:
    discount=0.0*amount
amount_discount=amount-discount
if member>50:
    final_amount=amount-(0.05*amount)
print("Final amount")
"""
# ============================================================