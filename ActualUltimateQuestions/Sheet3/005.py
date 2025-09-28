# What code calculates the sum of digits in a number?
"""

"""
# How do you reverse a number using a while loop?
"""
n=int(input("Enter a number:  "))
while n>0:
    print(str(n)[::-1])
"""
# What while loop prints the first 10 multiples of a user-entered number?
"""
n=int(input("Enter a number:  "))
i=1
while i<=10:
    print(f"{n} multiplied with {i} is {n*i}")
    i+=1
"""
# How can you keep asking for a password until it matches "secret"?
"""
password=str(input("Enter the password:  "))
while password:
    if password=="Secret" or "secret":
        print("Password is valid")
    else:
        print("Incorrect password,Try another password")
"""
# What loop prints numbers from 1 to 50 that are divisible by 9?
for i in range(9,51,9):
    print(i)
# How do you print a countdown from n to 1, where n is user input?

# What while loop prints numbers until their sum exceeds 100?

# How can you print the digits of a number one per line?

# What code finds the number of iterations until a number becomes 1?

# (divide by 2 if even, multiply by 3 and add 1 if odd)?

# How do you print numbers from 1 to 10 with their factorials?
