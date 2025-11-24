# Error Handling --- 
# Memory , Hardware , Logical Error , Keyboard Interupt  
# print(x)
# print("'x' is not defined")

# try except else finally
# 
#  try -- This is the block of code that i actually want to execute 

# except --  If there is an error in try except will be executed 

"""
try:
    print(40)
except:
    print("'x' is not defined")

# if else -- 

else:
    print("No error occured")
finally: 
    print("I don't care about errors")
"""


"""

def readFile(Filepath):
    try:
        file = open(Filepath,'r')
    except FileNotFoundError:
        print("File not found")
    else:
        content = file.read()
        print("File Contrent: ", content)
    finally:
        file.close()

readFile('../FileHandling/mytext1.txt')

"""
def division():
    try:
        a = int(input("Enter first number :"))
        b = int(input("Enter second number : "))
        result = a/b 
        print("result",result)
    except (ValueError,ZeroDivisionError) as err:
        print("Error: ", err)

division()