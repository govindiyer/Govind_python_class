# Python Fundamentals Assessment

## Topics Covered

Introduction, Syntax, Comments, Variables, Data Types, Numbers, Casting, Strings, Booleans

**Instructions**

1. Do not run the code immediately.
2. Predict the output first.
3. Explain your reasoning wherever possible.
4. For debugging questions, identify the issue and provide a correction.
5. Marks should be awarded based on understanding, not memorization.

---

# Section A: Conceptual Understanding

### 1.

Why is Python called an interpreted language?

### 2.

What happens when Python encounters a syntax error?

### 3.

Why is indentation important in Python?

### 4.

What is the difference between a variable and a value?

### 5.

Can a variable change its data type during execution? Explain with an example.

### 6.

Why does Python not require explicit variable type declarations?

### 7.

What is dynamic typing?

### 8.

What is the difference between a compiler and an interpreter?

### 9.

Why are comments important in real-world software projects?

### 10.

When would you use multi-line comments instead of single-line comments?

---

# Section B: Predict the Output

### 11.

```python
print("Hello")
print("World")
```

### 12.

```python
x = 10
print(x)
```

### 13.

```python
x = 10
x = 20
print(x)
```

### 14.

```python
name = "Arvinder"
print("Hello", name)
```

### 15.

```python
x = y = z = 100
print(x, y, z)
```

### 16.

```python
a, b, c = 1, 2, 3
print(c, a, b)
```

### 17.

```python
x = 5
y = "5"
print(x == y)
```

### 18.

```python
print(type(10))
```

### 19.

```python
print(type(10.5))
```

### 20.

```python
print(type("10"))
```

---

# Section C: Variables and Data Types

### 21.

What will happen?

```python
x = 10
print(y)
```

### 22.

What is the data type of the following variable?

```python
x = True
```

### 23.

What is the data type of the following variable?

```python
x = 10j
```

### 24.

Explain the difference between:

```python
x = 10
```

and

```python
x = "10"
```

### 25.

Can a variable name start with a number? Why or why not?

### 26.

Which of the following are invalid variable names?

```python
2name
first-name
_name
name123
class
```

### 27.

What is the purpose of the `type()` function?

### 28.

How would you check the type of a variable named `salary`?

### 29.

What data type is produced by:

```python
x = 5 / 2
```

### 30.

What data type is produced by:

```python
x = 5 // 2
```

---

# Section D: Debugging

### 31.

Find the error and correct it.

```python
print("Hello)
```

### 32.

Find the error and correct it.

```python
if True:
print("Hello")
```

### 33.

Find the error and correct it.

```python
1name = "John"
```

### 34.

Find the error and correct it.

```python
print(Hello)
```

### 35.

Find the error and correct it.

```python
x = 10
print(x
```

### 36.

Find the error and correct it.

```python
name = "John"
print(Name)
```

### 37.

What error will this produce?

```python
print(10 / 0)
```

### 38.

What error will this produce?

```python
int("abc")
```

### 39.

What error will this produce?

```python
float("hello")
```

### 40.

What error will this produce?

```python
print(age)
```

---

# Section E: Strings

### 41.

Predict the output.

```python
name = "Python"
print(name[0])
```

### 42.

Predict the output.

```python
name = "Python"
print(len(name))
```

### 43.

Predict the output.

```python
txt = "hello world"
print(txt.upper())
```

### 44.

Predict the output.

```python
txt = "HELLO"
print(txt.lower())
```

### 45.

What is the difference between:

```python
"Python"
```

and

```python
'Python'
```

### 46.

How can you create a string that spans multiple lines?

### 47.

Predict the output.

```python
txt = "Python"
print(txt[-1])
```

---

# Section F: Booleans and Logical Thinking

### 48.

Predict the output.

```python
print(bool("Hello"))
```

### 49.

Predict the output.

```python
print(bool(""))
```

### 50.

Predict the output and explain why.

```python
x = 10

if x:
    print("Valid")
else:
    print("Invalid")
```

---

# Bonus Understanding Questions

### 51.

Why does `bool("")` return `False` while `bool("0")` returns `True`?

### 52.

Why is `10` considered `True` inside an `if` statement?

### 53.

Why can Python store a string in a variable that previously stored an integer?

### 54.

What problems could occur if Python ignored indentation?

### 55.

Why is `"5" + "5"` different from `5 + 5`?

### 56.

What is the difference between:

```python
int(5.9)
```

and

```python
round(5.9)
```

### 57.

Why does `type(True)` return `bool` instead of `int`?

### 58.

Explain variables to a non-technical person using a real-life example.

### 59.

If Python automatically creates variables when assigned, what kinds of mistakes can programmers make?

### 60.

Explain the concept of a data type in a simple way.






print("ANSWERSSS")
# # Python Fundamentals Assessment

# ## Topics Covered

# ---

# # Section A: Conceptual Understanding

# ### 1.

# Why is Python called an interpreted language?
#Python is called an interpreted language because every code can be run and tested again and again until you get the output you desire

# ### 2.

# What happens when Python encounters a syntax error?
#When Python encounters a syntax error, it tells the ser that a certain piece of code has a syntax error and you have to run it again from the start

# ### 3.

# Why is indentation important in Python?
#Indentation is important in python becase withot it, mltiple topics/stratergies which make our coding easier like loops, functions, etc will be non-existent as they require indentation to run properly

# ### 4.

# What is the difference between a variable and a value?
#Values is a data type that is fixed,eg:2,"Hello",True,etc. Variables are data types whose values can vary,eg:x,a,p,etc.


# ### 5.

# Can a variable change its data type during execution? Explain with an example.
#Yes, a variable can change it's data type during execution.eg:
#x="5"
#print(int(x))Output: 5

# ### 6.

# Why does Python not require explicit variable type declarations?
#Python does not require explicit type deaclarations because, the computer can realize the variable's data type.

# ### 7.

# What is dynamic typing?
#Dynamic typing is when you give a value to a variable without explicitly declaring it as it's type.

# ### 8.

# What is the difference between a compiler and an interpreter?
#Compiler: runs the code and prints the output.
#Interpreter: Predicts the output

# ### 9.

# Why are comments important in real-world software projects?
#Comments are important in real-world software projects because the pregrammer can understand that what is the main purpose of a certain piece of code.

# ### 10.

# When would you use multi-line comments instead of single-line comments?
#you shpud use multi-line comments when the code takes up a lot of space/ a lot of lines.

# ---

# # Section B: Predict the Output

# ### 11.

# ```python
# print("Hello")
# print("World")
#Hello
#World
# ```

# ### 12.

# ```python
# x = 10
# print(x)
#10
# ```

# ### 13.

# ```python
# x = 10
# x = 20
# print(x)
#20
# ```

# ### 14.

# ```python
# name = "Arvinder"
# print("Hello", name)
#Hello Arvinder
# ```

# ### 15.

# ```python
# x = y = z = 100
# print(x, y, z)
#100 100 100
# ```

# ### 16.

# ```python
# a, b, c = 1, 2, 3
# print(c, a, b)
#3 1 2
# ```

# ### 17.

# ```python
# x = 5
# y = "5"
# print(x == y)
#False
# ```

# ### 18.

# ```python
# print(type(10))
#int
# ```

# ### 19.

# ```python
# print(type(10.5))
#float
# ```

# ### 20.

# ```python
# print(type("10"))
#str
# ```

# ---

# # Section C: Variables and Data Types

# ### 21.

# What will happen?

# ```python
# x = 10
# print(y)
#Name error, y is not defined
# ```

# ### 22.

# What is the data type of the following variable?

# ```python
# x = True
#Boolean
# ```

# ### 23.

# What is the data type of the following variable?

# ```python
# x = 10j
#Complex number
# ```

# ### 24.

# Explain the difference between:

# ```python
# x = 10
# ```->Integer

# and

# ```python
# x = "10"
# ```->String

# ### 25.

# Can a variable name start with a number? Why or why not?
#No, because if you do, python will return an error

# ### 26.

# Which of the following are invalid variable names?

# ```python
# 2name :::
# first-name :::
# _name
# name123
# class
# ```

# ### 27.

# What is the purpose of the `type()` function?
#To print the data type of a variable or value

# ### 28.

# How would you check the type of a variable named `salary`?
#print(typer(salary))

# ### 29.

# What data type is produced by:

# ```python
# x = 5 / 2
#float
# ```

# ### 30.

# What data type is produced by:

# ```python
# x = 5 // 2
#int
# ```

# ---

# # Section D: Debugging

# ### 31.

# Find the error and correct it.

# ```python
# print("Hello")
# ```

# ### 32.

# Find the error and correct it.

# ```python
# if True:
#   print("Hello")
# ```

# ### 33.

# Find the error and correct it.

# ```python
# name1 = "John"
# ```

# ### 34.

# Find the error and correct it.

# ```python
# print("Hello")
# ```

# ### 35.

# Find the error and correct it.

# ```python
# x = 10
# print(x)
# ```

# ### 36.

# Find the error and correct it.

# ```python
# name = "John"
# print(name)
# ```

# ### 37.

# What error will this produce?

# ```python
# print(10 / 0)
#value error

# ```

# ### 38.

# What error will this produce?

# ```python
# int("abc")
#value error

# ```

# ### 39.

# What error will this produce?

# ```python
# float("hello")
#value error

# ```

# ### 40.

# What error will this produce?

# ```python
# print(age)
#name error

# ```

# ---

# # Section E: Strings

# ### 41.

# Predict the output.

# ```python
# name = "Python"
# print(name[0])
#P

# ```

# ### 42.

# Predict the output.

# ```python
# name = "Python"
# print(len(name))
#6

# ```

# ### 43.

# Predict the output.

# ```python
# txt = "hello world"
# print(txt.upper())
#HELLO WORLD

# ```

# ### 44.

# Predict the output.

# ```python
# txt = "HELLO"
# print(txt.lower())
#hello

# ```

# ### 45.

# What is the difference between:

# ```python
# "Python"
# ```

# and None, they have the same purpose, but the quoatation's symbol is the same

# ```python
# 'Python'
# ```

# ### 46.

# How can you create a string that spans multiple lines?
#print the string in back-to-back-to-back-... how many ever times you want

# ### 47.

# Predict the output.

# ```python
# txt = "Python"
# print(txt[-1])
#n

# ```

# ---

# # Section F: Booleans and Logical Thinking

# ### 48.

# Predict the output.

# ```python
# print(bool("Hello"))
#True 
 
#```

# ### 49.

# Predict the output.

# ```python
# print(bool(""))
#False 

# ```

# ### 50.

# Predict the output and explain why.

# ```python
# x = 10

# if x:
#     print("Valid")
# else:
#     print("Invalid")
#Output: valid, because x is true 

# ```

# ---

# # Bonus Understanding Questions

# ### 51.

# Why does `bool("")` return `False` while `bool("0")` returns `True`?
#Because an empty string returs false whereas any string that has a value or variable that have a non-empty string is true

#  ### 52.

# Why is `10` considered `True` inside an `if` statement?
#because any number other than 0 is True

# ### 53.

# Why can Python store a string in a variable that previously stored an integer?
#because, a variable can change in both values and data types.

# ### 54.

# What problems could occur if Python ignored indentation?
#Loops, Functions,etc will not work

# ### 55.

# Why is `"5" + "5"` different from `5 + 5`?
#"5" + "5" returns 55, while 5+5 returns 10

# ### 56.

# What is the difference between:

# ```python
# int(5.9)
# ``` returns 5

# and

# ```python
# round(5.9)
# ``` returns 6

# ### 57.

# Why does `type(True)` return `bool` instead of `int`?
#because True is a bool val, not int

# ### 58.

# Explain variables to a non-technical person using a real-life example.
#John has 3 apples, he goes and tells the cashier to give him 2 more apples. This means that variables can change values

# ### 59.

# If Python automatically creates variables when assigned, what kinds of mistakes can programmers make?

# ### 60.

# Explain the concept of a data type in a simple way.
# A data type is type of a value.eg: 5-> int, "gred"->str
