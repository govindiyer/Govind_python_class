#Write a code that takes a list with 10 random numbers, find count of even numbers present
"""
list=[]

count=0
for i in range(10):
    n=int(input("Enter a number: "))
    list.append(n)
print(list)
for j in list:
    if j%2==0:
        count+=1
print(count)
"""
#Write a code with 3 funtions a,b,c where a calls b and b calls c
def a():
    print("a")
    b()
def b():
    print("b")
    c()  
def c():
    print("c")
a()

