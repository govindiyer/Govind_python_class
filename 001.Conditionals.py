# Sequential Execution 

# Top to bottom approach 

# print("Hello")
# print(456)
# print("Hello Again")
# print(4569)

#block -- {}

# if condition is true then one block of code will be executed else it will execute the other block

# if elif else -- Keywords
# if condtion:
#     #this will be executed 
# else:
#     # otherwise this will be executed 

# if True:
#     print("it is True")
# if False:
#     print("it will be skipped because it is not True")


# if True:
#     print("It is true")
# else:
#     print("It is false")

# What are true values :
# True , Any number (positive , negative except 0), "Anystring" except empty string
if 4:
    print("It is true")
else:
    print("It is false")

if -4:
    print("It is true")
else:
    print("It is false")
    
if "hello":
    print("It is true")
else:
    print("It is false")
if True:
    print("It is true")
else:
    print("It is false")
    

# False     
if "":
    print("It is true")
else:
    print("It is false")

if 0:
    print("It is true")
else:
    print("It is false")

if False:
    print("It is true")
else:
    print("It is false")

if 4>3:
    print("It is true")
else:
    print("It is false")
    
if 4==4:
    print("It is true")
else:
    print("It is false")

if 4>4:
    print("It is true")
else:
    print("It is false")
    
if 1==1.0:
    print("It is true")
else:
    print("It is false")
    
    
# if elif .... else -- If else ladder 

# marks = 60
marks = 90
if marks>90:
    print("A")
elif marks>80:
    print("B")
elif marks>70:
    print("C")
elif marks>55:
    print("D")
else:
    print("Fail")


#  Match Case -- Switch Case
# day = 6
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
    

# day = 7
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Office Days")
#     case 6 |7:
#         print("Weekends")

day = (0,9)
match day:
    case (x,0):
        print("x -axis")
    case (0,y):
        print("y-axis")
