# ============================================================
# PYTHON PRACTICE SHEET
# ============================================================


# ============================================================
# QUESTION 1: NUMBER CLASSIFICATION
# ============================================================
#
# Write a function:
#
#     classify_number(n)
#
# The function should determine:
#
# 1. Whether the number is positive, negative, or zero.
# 2. Whether it is even or odd, if it is not zero.
# 3. Whether it is divisible by both 3 and 5.
# 4. Whether it is a prime number.
#
# Use a loop to determine whether the number is prime.
#
# Example:
#
# Input:
# 30
#
# Output:
# Positive
# Even
# Divisible by 3 and 5
# Not Prime
#
# Requirements:
#
# 1. Create at least one function.
# 2. Do not use any built in prime checking function.
# 3. Handle negative numbers correctly.
#
# Write your solution below:
#
# ------------------------------------------------------------


# ============================================================
# QUESTION 2: STUDENT RESULT ANALYZER
# ============================================================
#
# Write a function:
#
#     calculate_result(marks)
#
# The function should accept marks of 5 subjects.
#
# Calculate:
#
# 1. Total marks
# 2. Percentage
# 3. Grade
# 4. Pass or Fail
#
# Grade rules:
#
# 90 or above       -> A+
# 80 to 89          -> A
# 70 to 79          -> B
# 60 to 69          -> C
# 50 to 59          -> D
# Below 50          -> F
#
# A student passes only if they score at least 40 marks
# in EVERY subject.
#
# Example:
#
# Input:
# 85 72 91 66 78
#
# Output:
# Total: 392
# Percentage: 78.4
# Grade: B
# Result: Pass
# Write your solution below:
#
# ------------------------------------------------------------


# ============================================================
# QUESTION 3: MULTIPLICATION TABLE GENERATOR
# ============================================================
#
# Write a function:
#
#     print_table(n, limit)
#
# The function should print the multiplication table of n
# from 1 up to the given limit.
#
# Example:
#
# Input:
# Number: 7
# Limit: 10
#
# Output:
#
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 10 = 70
#
# Additional Requirements:
#
# 1. If the number is negative, display an appropriate message.
# 2. If the limit is zero or negative, display an error.
# 3. Ask the user whether they want to generate another table.
# 4. Continue until the user enters "no".

#
# Write your solution below:
#
# ------------------------------------------------------------


# ============================================================
# QUESTION 4: PRIME NUMBERS IN A RANGE
# ============================================================
#
# Create a function:
#
#     is_prime(n)
#
# The function should return True if n is prime
# and False otherwise.
#
# Then create another function:
#
#     print_primes(start, end)
#
# This function should print all prime numbers between
# start and end.
#
# Example:
#
# Input:
# Start: 10
# End: 30
#
# Output:
# 11 13 17 19 23 29
#
# Total Prime Numbers: 6

# Write your solution below:
#
# ------------------------------------------------------------


# ============================================================
# QUESTION 5: ATM SIMULATION
# ============================================================
#
# Create a simple ATM program.
#
# Start with:
#
#     balance = 10000
#
# Create the following functions:
#
#     check_balance()
#     deposit(amount)
#     withdraw(amount)
#
# Display the following menu repeatedly:
#
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
#
# Rules:
#
# Deposit:
# The amount must be greater than zero.
#
# Withdrawal:
# The amount must be greater than zero.
# The user cannot withdraw more than the available balance.
#
# The program should continue until the user selects Exit.
#
# Example:
#
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
#
# Enter choice: 3
# Enter amount: 2500
#
# Withdrawal successful
# Remaining Balance: 7500
#
# Concepts:
#
# Functions
# While loop
# If/elif/else
# Input validation
# Variables
#
# Write your solution below:
#
# ------------------------------------------------------------


# ============================================================
# QUESTION 6: NUMBER GUESSING GAME
# ============================================================
#
# Create a number guessing game.
#
# Use:
#
#     secret_number = 47
#
# The user gets a maximum of 7 attempts.
#
# Create a function:
#
#     check_guess(guess, secret_number)
#
# The function should tell the user:
#
#     Too High
#     Too Low
#     Correct
#
# If the user guesses correctly, stop the game immediately.
#
# If all 7 attempts are used, display:
#
#     Game Over
#     The number was 47
#
# Example:
#
# Attempt 1
# Enter guess: 60
# Too High
#
# Attempt 2
# Enter guess: 30
# Too Low
#
# Attempt 3
# Enter guess: 47
# Correct
# You won!
#
# Additional Challenge:
#
# After the game finishes, ask:
#
#     Play Again? yes/no
#
# Allow the user to play multiple games.
#
# Write your solution below:
#
# ------------------------------------------------------------


# ============================================================
# QUESTION 7: SHOPPING CART BILL CALCULATOR
# ============================================================
#
# Create a program that calculates a shopping bill.
#
# Ask the user to enter the price of each item one by one.
#
# Continue accepting prices until the user enters:
#
#     0
#
# Create a function:
#
#     calculate_bill(total)
#
# Apply discounts using these rules:
#
# Total < 1000
# No discount
#
# 1000 to 4999
# 10% discount
#
# 5000 to 9999
# 20% discount
#
# 10000 or above
# 30% discount
#
# Calculate:
#
# Total Amount
# Discount
# Final Bill
#
# Example:
#
# Enter item price: 2000
# Enter item price: 1500
# Enter item price: 1000
# Enter item price: 0
#
# Total: 4500
# Discount: 450
# Final Bill: 4050
#
# Also display:
#
# Number of Items
# Highest Item Price
# Lowest Item Price
#
# Write your solution below:
#
# ------------------------------------------------------------


# ============================================================
# QUESTION 8: EMPLOYEE SALARY CALCULATOR
# ============================================================
#
# Create a function:
#
#     calculate_salary(basic_salary, experience)
#
# Calculate HRA using these rules:
#
# Basic < 30000
# HRA = 20% of Basic
#
# 30000 to 59999
# HRA = 25% of Basic
#
# 60000 or above
# HRA = 30% of Basic
#
# Calculate Experience Bonus:
#
# Experience < 2 years
# Bonus = 5% of Basic
#
# 2 to 5 years
# Bonus = 10% of Basic
#
# More than 5 years
# Bonus = 20% of Basic
#
# Calculate:
#
# Basic Salary
# HRA
# Experience Bonus
# Gross Salary
#
# Example:
#
# Basic Salary: 50000
# Experience: 4
#
# HRA: 12500
# Bonus: 5000
# Gross Salary: 67500
#
# Additional Challenge:
#
# Ask for multiple employees.
#
# At the end display:
#
# Total Employees
# Highest Gross Salary
# Lowest Gross Salary
# Average Gross Salary
#
# Write your solution below:
#
# ------------------------------------------------------------


# ============================================================
# QUESTION 9: MENU DRIVEN NUMBER ANALYZER
# ============================================================
#
# Create a menu driven program using functions.
#
# Display:
#
# 1. Check Even/Odd
# 2. Check Prime
# 3. Find Factorial
# 4. Find Sum of Digits
# 5. Reverse Number
# 6. Check Palindrome
# 7. Exit
#
# Create a separate function for each operation:
#
#     is_even(n)
#     is_prime(n)
#     factorial(n)
#     sum_of_digits(n)
#     reverse_number(n)
#     is_palindrome(n)
#
# Example:
#
# Enter number: 121
#
# 1. Check Even/Odd
# 2. Check Prime
# 3. Find Factorial
# 4. Find Sum of Digits
# 5. Reverse Number
# 6. Check Palindrome
# 7. Exit
#
# Enter choice: 6
#
# 121 is a Palindrome
# Write your solution below:
#
# ------------------------------------------------------------


# ============================================================
# QUESTION 10: COMPLETE STUDENT PERFORMANCE SYSTEM
# ============================================================
#
# Build a complete student performance analysis program.
#
# The program should allow the user to enter information
# for multiple students.
#
# For every student, enter:
#
#     Student Name
#     Marks in 5 Subjects
#
# Create the following functions:
#
#     calculate_total(marks)
#     calculate_percentage(total)
#     calculate_grade(percentage)
#     check_result(marks)
#
# Grade rules:
#
# 90+       -> A+
# 80 to 89  -> A
# 70 to 79  -> B
# 60 to 69  -> C
# 50 to 59  -> D
# Below 50  -> F
#
# A student fails if ANY subject is below 40.
#
# For every student display:
#
#     Student Name
#     Total
#     Percentage
#     Grade
#     Pass/Fail
#
# Example:
#
# How many students? 3
#
# Student 1
# Name: Rahul
# Marks: 85 76 91 88 79
#
# Student 2
# Name: Aman
# Marks: 35 72 65 80 71
#
# Student 3
# Name: Simran
# Marks: 92 94 89 91 95
#
# At the end display:
#
#     Total Students
#     Number of Passed Students
#     Number of Failed Students
#     Highest Percentage
#     Lowest Percentage
#     Average Percentage
#     Number of A+ Students
#     Number of A Students
#     Number of B Students
#     Number of C Students
#     Number of D Students
#     Number of F Students
# ------------------------------------------------------------