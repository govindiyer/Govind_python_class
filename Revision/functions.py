# Functions -- 

# Print Username 
# print("Hello Govind")

# print("Hello Govind")

# def Print():
#     print("Hello Govind")

# Print()
# Print()

# def Print(username):
#     print("Hello ",username)

# Print("Govind")
# Print("Arvinder")



# Two types of Functions -- Built in Functions , User Defined Function 

# print() , len() , type() , chr() , ord() , int() , input()

# User Defined Function -- 

# Return  -- 

def Add(a ,b):
    result = a+b
    return result
    # print(result)

# print(result)
# print(Add(20,30))

# x = Add(30,20)
# print(x)



# Calling a function inside another function 

# def Print1():
#     print("Inside Print1 ")
#     Print2()
#     print("Finished")

# def Print2():
#     print("Inside Print2")
# Print1()


# function calling itself -- recursion 

# iterative Approach -- Loops 
# initialization 
"""
i=1
while i <=5: #condition check 
    print(i)
    i+=1     # increement (step)

# Recursive Approach -- Functions 
def PrintNumbers(n):
    # Base Condition
    if n >5:
        return 
    print(n)

    # Recursive Call 
    PrintNumbers(n+1)
PrintNumbers(1)
"""

"""
# 10 9 8 7 6 5 4 3 2 1 
def PrintNumbers(n):
    if n < 1:
        return 
    print(n)
    # Recursive Call 
    PrintNumbers(n - 1)
PrintNumbers(10)

"""

# 10 + 9 --- + 1 

# looping -- 1 + 2 + 3 + 4 + 5 --- + 10 

# Recursive -- 1 + (Rest of the 9) --- 1 + 2 + (rest of 8) -- 