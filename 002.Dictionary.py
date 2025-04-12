# Dictionary -- Key - value based data strcuture 

myDictionary ={
    "Name":"Govind",
    "Age":14,
    "City":"Bangalore"
    # "Age":"Sirsa"
}
# print(myDictionary)

# Mutable -- Means we can modify the existing elements

# Unordered data structure 

# Keys should be unique 

# How to access a particular element

print(myDictionary['Age'])
print(myDictionary.get("Age"))
# How to update an existing element 
myDictionary['Age'] = 16
print(myDictionary['Age'])
print(myDictionary)


# Clear() -- TO empty a list 
# myDictionary.clear()
# print(myDictionary)

# To delete a dictionary 

# del myDictionary
# print(myDictionary)


# Copy all the elements of an existing dictionary to another dictionary
# myDictionary2 ={
#     "Name":"Govind",
#     "Age":16,
#     "City":"Bangalore"
#     # "Age":"Sirsa"
# }
# myDictionary3 = myDictionary
# print(myDictionary2 == myDictionary)
# print(myDictionary3)

# TO get all the keys of the dictionary
print(myDictionary.keys())

# to get all the values 
print(myDictionary.values())

# TO fetch both values and keys 
print(myDictionary)
print(myDictionary.items())


# len function 
print(len(myDictionary))

# TO remove a specific element

print(myDictionary.pop("Age"))

print(len(myDictionary))
print(myDictionary)

myDictionary.update({"Marks":97})
print(myDictionary)
# popitem
print(myDictionary.popitem())
print(myDictionary)


dictionaryNew = {}
print(dictionaryNew)
dictionary2 = dict()
print(dictionary2)

keys = [1,2,3,4,5]
newDictionary =dictionaryNew.fromkeys(keys,0)
print(newDictionary)
