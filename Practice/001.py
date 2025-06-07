# Write a program that prints the sum even and odd numbers from a list

def number_sum(myList):
    sumEven = 0
    sumOdd = 0
    for i in range(len(myList)):
        if myList[i]%2==0:
            sumEven+=myList[i]
        else:
            sumOdd+=myList[i]
    print("Even number total:" ,sumEven,"Odd Number total: ",sumOdd)

myList = [12,34,23,26,27,2,1,23,69,79]
# number_sum(myList)

myData = {
    "Student":{
        "Name":"Govind",
        "Age":12,
        "Course":"Python",
        "Hobbies":["Cricket","Video games","Coding","Music"]
    },
    "Country":"India",
    "Pincode":123456  
}

# print(myData)
# get the country name 
# print(myData.get('Country'))
# Get the student name:
# print(myData['Student']['Name'])


# Get the video games Hobby
# print(myData['Student']['Hobbies'][1])


nestedList = ["Netsed List",1256,{"Name":"Govind","Age":12,"Course":"Python","Hobbies":["Cricket","Video games","Coding","Music"]}, "India",123456]

# get me the string Nested List
print(nestedList[0])

# get me the stduent name
print(nestedList[2]['Name'])

# Get the video games Hobby
print(nestedList[2]['Hobbies'][1])

# Append a value to the Hobbies "Singing"

nestedList[2]['Hobbies'].append("Singing")
print(nestedList[2]['Hobbies'])
del nestedList[2]["Course"]
print(nestedList[2])



