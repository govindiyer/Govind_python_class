# ============================================================
# PYTHON PATTERN PROGRAMMING TEST
# ============================================================
# Total Questions: 17
# Section A: 10 Multiple Choice Questions
# Section B: 5 True or False Questions
# Section C: 2 Coding Questions
#
# Student Name: __________________________
# Date: __________________________________
#
# Instructions:
# 1. Read each question carefully.
# 2. For MCQs, write the correct option in the answer space.
# 3. For True or False, write True or False in the answer space.
# 4. For coding questions, complete the code area provided.
# 5. Code snippets are commented or separated clearly to help you
#    understand which code belongs to each question.
# 6. No answers are included in this test file.
# ============================================================


# ============================================================
# SECTION A: MULTIPLE CHOICE QUESTIONS
# ============================================================


# ------------------------------------------------------------
# Q1. Which code prints five stars on the same line?
#
# Pattern:
# *****
#
# Answer: Write here.
#
# A.
# print("*")
#
# B.
# print("*" * 5)              
#
# C.
# print("*" + 5)
#
# D.
# print(5 * "\n")
# ------------------------------------------------------------
# Option B

# ------------------------------------------------------------
# Q2. Which code prints the following square when n = 4?
#
# Pattern:
# ****
# ****
# ****
# ****
#
# Answer: Write here.
#
# A.
# for i in range(n):
#     print("*" * i)
#
# B.
# for i in range(n):
#     print("*" * n)
#
# C.
# for i in range(n):
#     print("*")
#
# D.
# for i in range(1, n):
#     print("*" * i)
# ------------------------------------------------------------
# Option B

# ------------------------------------------------------------
# Q3. Which code prints the following increasing triangle?
#
# Pattern:
# *
# **
# ***
# ****
#
# Answer: Write here.
#
# A.
# for i in range(4, 0, -1):
#     print("*" * i)
#
# B.
# for i in range(1, 5):
#     print("*" * i)
#
# C.
# for i in range(1, 5):
#     print("*" * 4)
#
# D.
# for i in range(4):
#     print("*" * i)
# ------------------------------------------------------------
# Option B

# ------------------------------------------------------------
# Q4. What is the output of the following code?
#
# n = 4
#
# for i in range(n, 0, -1):
#     print("*" * i)
#
# Pattern:
# Write the output here.
# ****
# ***
# **
# *
# Answer: Write here.
#
# A.
# *
# **
# ***
# ****
#
# B.
# ****
# ***
# **
# *
#
# C.
# ****
# ****
# ****
# ****
#
# D.
# ***
# **
# *
# ------------------------------------------------------------
# Option B

# ------------------------------------------------------------
# Q5. Which code prints the following right-aligned increasing triangle?
#
# Pattern:
#    *
#   **
#  ***
# ****
#
# Answer: Write here.
#
# A.
# for i in range(1, 5):
#     print(" " * (4 - i) + "*" * i)
#
# B.
# for i in range(1, 5):
#     print(" " * i + "*" * i)
#
# C.
# for i in range(4, 0, -1):
#     print(" " * (4 - i) + "*" * i)
#
# D.
# for i in range(1, 5):
#     print("*" * i)
# ------------------------------------------------------------
# Option A

# ------------------------------------------------------------
# Q6. Which code prints the following hollow square?
#
# Pattern:
# *****
# *   *
# *   *
# *   *
# *****
#
# Answer: Write here.
#
# A.
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()
#
# B.
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#
# C.
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#
# D.
# n = 5
# for i in range(n):
#     print("*" * i)
# ------------------------------------------------------------
# Option C

# ------------------------------------------------------------
# Q7. What is the output of the following code?
#
# for i in range(1, 5):
#     print(str(i) * i)
#
# Pattern:
# Write the output here.
#
# Answer: Write here.
#
# A.
# 1
# 12
# 123
# 1234
#
# B.
# 1
# 22
# 333
# 4444
#
# C.
# 1
# 11
# 111
# 1111
#
# D.
# 1111
# 2222
# 3333
# 4444
# ------------------------------------------------------------
# Option B

# ------------------------------------------------------------
# Q8. Which code prints the following increasing number triangle?
#
# Pattern:
# 1
# 12
# 123
# 1234
# 12345
#
# Answer: Write here.
#
# A.
# for i in range(1, 6):
#     print(i)
#
# B.
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
#
# C.
# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
#
# D.
# for i in range(1, 6):
#     print(str(i) * i)
# ------------------------------------------------------------
# Option A

# ------------------------------------------------------------
# Q9. Which code prints the following checkerboard pattern?
#
# Pattern:
# 10101
# 01010
# 10101
# 01010
# 10101
#
# Answer: Write here.
#
# A.
# for i in range(5):
#     for j in range(5):
#         print((i + j) % 2, end="")
#     print()
#
# B.
# for i in range(5):
#     for j in range(5):
#         print((i + j + 1) % 2, end="")
#     print()
#
# C.
# for i in range(5):
#     print("10101") NO
#
# D.
# for i in range(5):
#     print("1" * 5) NO
# ------------------------------------------------------------
# Option B

# ------------------------------------------------------------
# Q10. Which code prints the following alphabet triangle?
#
# Pattern:
# A
# AB
# ABC
# ABCD
# ABCDE
#
# Answer: Write here.
#
# A.
# for i in range(1, 6):
#     print(chr(64 + i) * i)
#
# B.
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(chr(64 + j), end="")
#     print()
#
# C.
# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(chr(64 + j), end="")
#     print()
#
# D.
# for i in range(1, 6):
#     print(chr(64 + i))
# ------------------------------------------------------------
# Option B

# ============================================================
# SECTION B: TRUE OR FALSE
# ============================================================


# ------------------------------------------------------------
# Q11. The following code prints five stars on the same line.
#
# Pattern:
# *****
#
# Code:
# for i in range(5):
#     print("*", end="")
#
# Answer: Write True or False here.
# ------------------------------------------------------------
# False

# ------------------------------------------------------------
# Q12. The following code prints a decreasing triangle.
#
# Pattern:
# ****
# ***
# **
# *
#
# Code:
# for i in range(1, 5):
#     print("*" * i)
#
# Answer: Write True or False here.
# ------------------------------------------------------------
# False

# ------------------------------------------------------------
# Q13. The following code prints a square where each row contains
# its row number.
#
# Pattern:
# 1111
# 2222
# 3333
# 4444
#
# Code:
# for i in range(1, 5):
#     print(str(i) * 4)
#
# Answer: Write True or False here.
# ------------------------------------------------------------
# True

# ------------------------------------------------------------
# Q14. The following code prints a reverse alphabet triangle.
#
# Pattern:
# ABCDE
# ABCD
# ABC
# AB
# A
#
# Code:
# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(chr(64 + j), end="")
#     print()
#
# Answer: Write True or False here.
# ------------------------------------------------------------
# True

# ------------------------------------------------------------
# Q15. The following code prints a hollow left-aligned triangle.
#
# Pattern:
# *
# **
# * *
# *  *
# *****
#
# Code:
# n = 5
#
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#
# Answer: Write True or False here.
# ------------------------------------------------------------
# False

# ============================================================
# SECTION C: CODING QUESTIONS
# ============================================================


# ------------------------------------------------------------
# Q16. STAR PATTERN: INTERMEDIATE LEVEL
#
# Question:
# Write a Python program to print a hollow centered pyramid of stars.
#
# Assume n = 5.
#
# Pattern:
#     *
#    * *
#   *   *
#  *     *
# *********
#
# Answer: Write your code here.

# Hint:
# Use loops to manage the leading spaces and the positions of stars.
# Keep the last row completely filled with stars.
# ------------------------------------------------------------

# Write your solution below.
n=5
for i in range(n-1,-1,-1):
    for j in range(9):
        if i==0:
            print("*",end=" ")
        elif j==i or j==8-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# ============================================================
# Q17. NUMBER PATTERN: INTERMEDIATE LEVEL
# ============================================================
#
# Question:
# Write a Python program to print a palindromic number pyramid.
#
# Assume n = 5.
#
# Pattern:
#     1
#    121
#   12321
#  1234321
# 123454321
#
# Answer: Write your code here.
#
# Hint:
# Print increasing numbers from 1 to the row number, followed by
# decreasing numbers. Add leading spaces to center each row.
# ------------------------------------------------------------

# Write your solution below.
n=5
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

# ============================================================
# ANSWER SHEET
# ============================================================
#
# MCQs:
# Q1: _____   Q2: _____   Q3: _____   Q4: _____   Q5: _____
# Q6: _____   Q7: _____   Q8: _____   Q9: _____   Q10: _____
#
# True or False:
# Q11: __________
# Q12: __________
# Q13: __________
# Q14: __________
# Q15: __________
#
# Coding:
# Q16: Complete the code section above.
# Q17: Complete the code section above.
#
# ============================================================
# END OF TEST
# ============================================================
