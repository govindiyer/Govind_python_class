# ---------------------------------------------
# Example 1: Function Calling Another Function
# ---------------------------------------------

def Another():
    print("Another Print")

def Greet():
    print("Hello User")
    Another()
    print("GO ")

# Calling the greet function
Greet()

# ---------------------------------------------
# Example 2: Repeated Greeting
# ---------------------------------------------

def Greet():
    print("Good Morning")

# Calling the Greet function multiple times
for _ in range(6):
    Greet()

# ---------------------------------------------
# Example 3: Greeting with Custom Messages
# ---------------------------------------------

def Greet(msg):
    print("Good", msg)

# Calling the Greet function with different messages
greetings = ["Morning", "Afternoon", "Evening", "Night", "Day"]
for greet in greetings:
    Greet(greet)

# ---------------------------------------------
# Example 4: Adding Three Numbers (No Return)
# ---------------------------------------------

def AddNumbers(a, b, c):
    print(a + b + c)

AddNumbers(10, 20, 30)
AddNumbers(100, 200, 300)

# ---------------------------------------------
# Example 5: Adding Three Numbers (With Return)
# ---------------------------------------------

def AddNumbers(a, b, c):
    result = a + b + c
    return result

print(AddNumbers(10, 20, 30))

result = AddNumbers(100, 200, 300)
print(result)

# ---------------------------------------------
# Example 6: Calculating Average of Three Numbers
# ---------------------------------------------

def Avg(a, b, c):
    result = (a + b + c) / 3
    return result

print(Avg(10, 20, 30))

# ---------------------------------------------
# Example 7: Printing Full Name
# ---------------------------------------------

def Fullname(fname, lname):
    print(f"{fname} {lname}")

Fullname("Govind", "Python")

# ---------------------------------------------
# Example 8: Sum of All Elements in List
# ---------------------------------------------

def SumList(li):
    result = sum(li)
    return result

l = [10, 20, 29, 36, 74, 94, 50]
print(SumList(l))

# ---------------------------------------------
# Example 9: Sum of Even Elements in List
# ---------------------------------------------

def EvenSum(li):
    result = sum(i for i in li if i % 2 == 0)
    return result

l = [10, 20, 29, 36, 74, 94, 50]
print(EvenSum(l))

# ---------------------------------------------
# Example 10: Product of Odd Elements in List
# ---------------------------------------------

def Product(li):
    result = 1
    for i in li:
        if i % 2 == 1:
            result *= i
    return result

l = [10, 21, 29, 36, 74, 94, 50]
print(Product(l))

# ---------------------------------------------
# Example 11: Difference Between Product and Sum
# ---------------------------------------------

def diff(li):
    prod = 1
    add = 0
    for i in li:
        prod *= i
        add += i
    return prod - add

l = [8, 1, 2, 6, 4, 4, 5]
print(diff(l))
