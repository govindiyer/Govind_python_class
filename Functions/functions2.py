# return keyword

def Sum(a,b):
  result = a+b 
  print("Result:",result)

# Sum(10,20)
# print(result) #NameError: name 'result' is not defined

# Scope -- global -- Common to everything we can use it anywhere 

# Local Scope -- Inside the function we can use it.

total = 1
def product(myList):
  global total
  for i in range(len(myList)):
    total*=myList[i]
  
  print(total)

myList = [1,2,2,3,5,5]
# product(myList)


def Sum(a,b):
  result = a+b
  print(result)
  return result
  # print("Result:",result)

# Return -- First returns a copy of the local variables 
# It represents the ending of the functions.
# Any code of line written after return keyword will not be executed

x = Sum(100,24)
print(x+100)

# Recursion -- A function can calls itself.
def Order(n):
  if n > 10:
    return 
  print(n)
  return Order(n+1)

Order(1)
