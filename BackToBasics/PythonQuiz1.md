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
