# 1. How to check if the value exists in Dictionary or not


"""
myDictionary = {"name":"Laptop","Brand":"Apple","Year":2000}
if "name" in myDictionary:
    print("Exists")
else:
    print("Does not exist")

if "Apple" in myDictionary:
    print("Exists")
else:
    print("Does not exist")


"""


# 2. Printing all the keys

# keys() -- For keys 
# values() -- For values 
# items() -- For Both keys and values
'''
myDictionary = {"name":"Laptop","Brand":"Apple","Year":2000}
keys =[]

for k in myDictionary:
    keys.append(k)

print(keys)
'''

# 3. Printing all values 

# keys() -- For keys 
# values() -- For values 
# items() -- For Both keys and values
"""
myDictionary = {"name":"Laptop","Brand":"Apple","Year":2000}
keys =[]

for k in myDictionary.values():
    keys.append(k)

print(keys)
"""
# 4. Printing keys and values both
"""
myDictionary = {"name":"Laptop","Brand":"Apple","Year":2000}
for k in myDictionary:
    print("Key:",k, "---- Value: ", myDictionary[k])
"""

# Len()

# 5. Count the number of elements in a list
"""
myDictionary = {"name":"Laptop","Brand":"Apple","Year":2000}
count =0
for k in myDictionary:
    count+=1

print(count)
"""

# 6. Copy a dictionary custom function 
"""
myDictionary = {"name":"Laptop","Brand":"Apple","Year":2000}
newDictionary = {}

# newDictionary = myDictionary
# myDictionary["NewItem"]=1000
# print(myDictionary)
# print(newDictionary)

for k, v in myDictionary.items():
    newDictionary[k]=v
print(myDictionary)

print(newDictionary)
"""

# 7. Merge Two Dictionaries
"""
myDictionary = {"name":"Laptop","Brand":"Apple","Year":2000} 
secondDictionary = {"First":123,"Second":2456}

finalDictionary = {}
for k , v in myDictionary.items():
    finalDictionary[k]=v 

for k , v in secondDictionary.items():
    finalDictionary[k]= v

print(finalDictionary)
"""

# 8. count occurences of a number in list

"""
myList = [1,2,3,4,1,2,3,8,5,0,2,4,7]
# 1: 2 , 2 :3 , 3:2 , 

freq = {}

# 1:2 , 2 :3 , 3:2 , 4:2 , 8:1,5:1 , 0:1 , 7:1
for x in myList:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] =1

print(freq)
"""

# 9. Print the sum of values of dictionary
"""
marks= {"Arvinder": 13,"Govind":78,"Someone":56}
total = 0

for v in marks.values():
    total+= v 

print(total)
"""

# 10. Count the occrence of a character in string 

"""
# "Hello World"  -- 
text = "Hello World"
freq = {}
for x in text:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] =1

print(freq)
"""






















