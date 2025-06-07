# -------------------------------------------
# 📘 PYTHON FUNCTIONS – COMPLETE NOTES
# -------------------------------------------

# ✅ What is a Function?
# A function is a reusable block of code that performs a specific task.

# -------------------------------------------
# 🧠 Real-World Analogy
# -------------------------------------------
# Think of a plumber: 
# We call the plumber to fix a water leak.
# Similarly, we call a function to perform a task.

# -------------------------------------------
# 🛠️ Defining a Function
# -------------------------------------------

def Greet():
    print("Hello Govind!")  # This is the function body

# 🏃 Calling the function
Greet()

# 🔁 Calling it multiple times
Greet()
Greet()

# ⚠️ Calling undefined function – this will throw an error
# Home()  # ❌ NameError

# ✅ Define the function before calling it
def Home():
    print("This is my home")

Home()

# -------------------------------------------
# ➕ Function with internal logic
# -------------------------------------------

def Add():
    a = 10 
    b = 20
    print("Sum:", a + b)

Add()

# -------------------------------------------
# 📦 Function with Parameters
# -------------------------------------------

def add(a, b):
    print("Sum:", a + b)

add(10.04, 20.05)
add(100, 200)
add(-300, -400)

# ❗ Common mistakes
# add(100)        # ❌ Missing one argument
# add(10, 20, 30) # ❌ Too many arguments
# Add(10, 20)     # ❌ Case-sensitive (if 'Add' is not defined)

# -------------------------------------------
# 💬 Scope of Variables
# -------------------------------------------

sum = 0

def AddLocal(a, b):
    sum = a + b
    print("Sum inside function:", sum)

AddLocal(10, 20)
print("Sum outside function:", sum)  # Global 'sum' remains 0

# -------------------------------------------
# 🔙 Return Statement
# -------------------------------------------

def Number(x):
    return x + 10  # Return a value instead of printing

x = 30
y = Number(x)
print("Returned value:", y)

def SumOfNumbers(a, b, c):
    result = a + b + c
    return result
    # Code after return is not executed:
    # print("This won't print")

x = SumOfNumbers(10, 20, 30) + 100
print("Final result:", x)

# -------------------------------------------
# 📥 User Input Inside Function
# -------------------------------------------

def GreetUser():
    name = input("Enter your name: ")
    print("Hi", name)

# Uncomment to run:
# GreetUser()

# -------------------------------------------
# 🧮 Sum of List Elements
# -------------------------------------------

def SumOfListElem(myList):
    total = 0 
    for i in range(len(myList)):
        total += myList[i]
    print("Total sum:", total)

myList = [12, 1, 3, 5, 60, 32, 25, 10]
SumOfListElem(myList)

# -------------------------------------------
# 🔁 Function Calling Another Function
# -------------------------------------------

def One():
    print("One")
    Three()  # Call another function

def Two():
    print("Two")

def Three():
    Two()    # Call another function
    print("Three")

# Uncomment to see the flow
# Three()
# One()

# -------------------------------------------
# 🔄 Updated Example With Execution Flow
# -------------------------------------------

def One():
    print("One")

def Two():
    print("Two")
    One()
    print("Inside Two()")

def Three():
    print("Three")
    Two()
    print("Inside Three()")

print("Starting")
Three()
print("Ending")

# -------------------------------------------
# 🧰 Built-in vs User-defined Functions
# -------------------------------------------

# Built-in functions
print("Example of built-in functions:")
print(len("Hello"))       # len()
print(type(123))          # type()
print(int("10"))          # int()

# User-defined function
def MyFunction():
    print("This is user-defined.")

MyFunction()
