# Python Loops: Concise Notes & Examples

# 1. For Loop
# Iterates over a sequence (list, string, range).
# Syntax: for var in sequence:
# Use when number of iterations is known.

# Example: Print numbers 0 to 4
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Example: Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry

# 2. While Loop
# Runs as long as condition is True.
# Syntax: while condition:
# Use when iterations depend on a condition.

# Example: Print 1 to 5
i = 1
while i <= 5:
    print(i)  # Output: 1, 2, 3, 4, 5
    i += 1

# Example: Infinite Loop (Commented to avoid execution)
# while True:
#     print("Infinite loop!")  # Runs forever unless stopped
#     break  # Added to prevent infinite run during testing

# 3. Loop Control Statements
# break: Exits loop.
# continue: Skips to next iteration.
# pass: Placeholder, does nothing.

# Example: Break at 3
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2

# Example: Skip 3 with continue
for i in range(5):
    if i == 3:
        continue
    print(i)  # Output: 0, 1, 2, 4

# Example: Pass as placeholder
for i in range(3):
    if i == 1:
        pass  # No action
    print(i)  # Output: 0, 1, 2

# 4. Else with Loops
# Runs if loop completes without break.

# Example: For loop with else
for i in range(3):
    print(i)
else:
    print("Loop done!")  # Output: 0, 1, 2, Loop done!

# 5. Nested Loops
# Loop inside a loop; inner loop runs fully for each outer iteration.

# Example: Print pairs
for i in [1, 2]:
    for j in [3, 4]:
        print(i, j)  # Output: 1 3, 1 4, 2 3, 2 4

# 6. Practical Examples

# Beginner: Sum of elements (1 to 5)
sum_nums = 0
for i in range(1, 6):
    sum_nums += i
print("Sum:", sum_nums)  # Output: Sum: 15

# Beginner: Product of elements in a list
numbers = [1, 2, 3, 4]
product = 1
for num in numbers:
    product *= num
print("Product:", product)  # Output: Product: 24

# Beginner: Print string in reverse using negative step
text = "Python"
for i in range(len(text)-1, -1, -1):
    print(text[i])  # Output: n, o, h, t, y, P

# Intermediate: Sum of even numbers (1 to 10)
even_sum = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        even_sum += i
    i += 1
print("Sum of evens:", even_sum)  # Output: Sum of evens: 30

# Intermediate: Factorial (product of 1 to 5)
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial of 5:", factorial)  # Output: Factorial of 5: 120

# Advanced: Sum of squares of odd numbers (1 to 10)
odd_square_sum = 0
for i in range(1, 11):
    if i % 2 == 1:
        odd_square_sum += i ** 2
print("Sum of odd squares:", odd_square_sum)  # Output: Sum of odd squares: 165

# Advanced: Product of elements at even indices
nums = [2, 3, 4, 5, 6]
even_index_product = 1
for i in range(0, len(nums), 2):
    even_index_product *= nums[i]
print("Product at even indices:", even_index_product)  # Output: Product at even indices: 48
