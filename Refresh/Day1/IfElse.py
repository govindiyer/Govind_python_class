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
# 0 to 100 units       -> ₹5 per unit
# 101 to 200 units     -> ₹7 per unit
# 201 to 300 units     -> ₹10 per unit
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

# ============================================================