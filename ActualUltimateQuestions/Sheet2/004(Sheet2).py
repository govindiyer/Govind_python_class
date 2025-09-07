# How do you write a program to check if a number is between 10 and 50 and divisible by 5 using logical AND?
"""
n=int(input("Enter a number:  "))
if n>10 and n<50 and n%5==0:
    print(f"The number {n} is between 10 and 50 and the number {n} is also divisible by 5")
"""
# What program uses logical OR to determine if a user-entered number is less than 0 or greater than 100?
"""
n=int(input("Enter a number:  "))
if n<0 or n>100:
    print(f"The number {n} is either smaller than zero or greater than hundred")
"""
# How can you use logical NOT in a program to print "Invalid" if a user-entered list is not empty?
"""
n=[]
if  len(n)>=1 :
    print("Invalid")
else:
    print("Valid")
"""
# What program checks if a user-entered character is a vowel and the length of a string is greater than 5 using AND?
"""
n=input("Enter a word:  ")
if n=="a" or "e" or "i" or "o" or "u" and len(n)>=5:
    print("Answer is correct ")
else:
    print("Answer is wrong, try another word")
"""
# How do you use logical operators to verify if a dictionary has more than 3 keys and all values are positive?
"""
n={"Key1":1,"Key2":2,"Key3":3,"Key4":4}
if(len(n)>3) and all(value>0 for value in n.values()):
    print("True")
"""
# How do you write a program to check if a user-entered number is even using a bitwise AND operator?
"""
n=int(input("Enter a number:  "))
if n&1==0:
    print("Even")
else:
    print("Odd")
"""
# What program uses a bitwise OR to combine two user-entered numbers and prints the result?
"""
n=int(input("Enter a number:  "))
n1=int(input("Enter another number:  "))
if True:
    print(n|n1)
else:
    print(n|n1)
"""
# How can you use a bitwise XOR in a program to swap two numbers without a temporary variable?
"""
x=5
y=10
print("Before Swapping:",x,",",y)
if True:
    x=x^y
    y=x^y
    x=x^y
print("After Swapping:",x,",",y)
"""  	
# What program checks if a number’s binary representation has a 1 in the second bit using bitwise AND?
"""
n=12  
n1=2     
r = n&n1
if r!= 0:
    print(f"The second bit of {n} is 1.")
else:
    print(f"The second bit of {n1} is 0.") 
"""   
# How do you use a bitwise left shift to double a user-entered number and print the result?
"""
n=int(input("Enter a number:  "))
if True:
    n1=n<<1
print(n1)
"""