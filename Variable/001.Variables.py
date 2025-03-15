# variables , 

# An entity whose value can change. -- Variable

# variable_name = value 
# We have declared a variable x and assigned a value to it.
x = 20
print(x)
# Declaration alone is not possible -- Python

# indentifier == variable_name

# Reassign a value to it.

# Sequential execution of code  -- Top to bottom execution
# x=30
# x ----------> 30

# y -----------> x
x = 40
y = x
x = y+ 20
y = x+30
print(x,y)

# 60 , 90

# Naming convention of variable
'''
1. Name should not start witha digit. Letters , _ 
3name , %age , 


2. Digits can come in between 
Age3, _age , age123

3. We should give only decriptive name. 
marks = 40 , age = 50 , x = 50 , 

4. Should not be lengthy --> ageOfhenryMarkson , age = 50 

5. We can't use keywords as variable names.

if = 30 X

'''

# When we should use x, y,z as variable names or when we should prefer descriptive names ?
# Answer : It depedns upon the life of the variable


# Why do we need variables at all ?
# x = 40 
# print(x)
# print(40)

# to print Hello World 10 times ?
def Greet(name):
    print("Good Morning,", name)

Greet("Arvinder")
Greet("Govind")
