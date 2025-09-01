print("Lists revision")
#Creating Lists
l=[1,2,3,"a","b","c"]
#Udating an element in a list
#1-
l[2]="d"
#Adding elements in a list
#1-At the end of a list
l.append("e")
#2-Wherever you want your eleentt to be in
l.insert(4,"f")
print(l)
#Removing elements from a list
#1-Removing an element at the end of a list
l.pop()
#2-Removing an element from a certain index of a list
l.pop(-4)

# 3-removing an element with a value(Will give error if not present in a list)
l.remove("a")
l.remove("G")#Will give error
# Clearing a list:
l.clear()
#Deleting a list:
"""
del l
"""

if 5 in l:
    print("Present")
else:
    print("Not present")

sum1=0
l=[3,8,7,5,4,9,0]
for i in l:
    sum1+=i
print(sum1)

sum1=1
l=[3,8,7,5,4,9]
for i in l:
    sum1*=i
print(sum1)

#Slicing-
#1-Positive Slicing
print(l[2:4])
print(l[1:4])
#2-Negative Slicing
print(l[-2:-4])  
print(l[-1:-4])

