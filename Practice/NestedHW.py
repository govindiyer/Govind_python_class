myData= {
  "Tutor": "Arvinder Pal",
  "Mode": "Online",
  "Bootcamp": "Online Python Course",
  "data": {
    "studentProfile": {
      "personalInfo": {
        "name": "Govind Iyer",
        "age": 12,
        "grade": 7,
        "studentId": "STU123456",
        "dateOfBirth": "2012-04-15",
        "nationality": "Indian",
        "languages": ["English", "Hindi", "Kannada"],
        "contact": {
          "email": "govind.sharma@example.com",
          "phone": "+91-9876543210",
          "address": {
            "street": "123 MG Road",
            "city": "Bangalore",
            "state": "Karnataka",
            "country": "India",
            "pincode": 123456
          },
          "emergencyContact": {
            "name": "Smrithi Aparajithan",
            "relationship": "Mother",
            "phone": "+91-9686938909"
          }
        }
      },
      "academicInfo": {
        "course": "Python Programming",
        "enrollmentDate": "2024-09-01",
        "progress": {
          "modulesCompleted": 8,
          "totalModules": 20,
          "percentage": 40.0
        },
        "grades": [
          {"module": "Basics", "score": 85},
          {"module": "Functions", "score": 78},
          {"module": "Data Structures", "score": 92}
        ],
        "attendance": {
          "totalClasses": 50,
          "classesAttended": 48,
          "attendancePercentage": 96.0
        }
      },
      "hobbies": ["Cricket", "Video Games", "Coding", "Music", "Chess","Basketball"],
      "extracurricular": [
        {
          "activity": "Cricket Club",
          "role": "Member",
          "achievements": ["Best Batsman 2024"],
          "activeSince": "2023-06-01"
        },
        {
          "activity": "Coding Club",
          "role": "Junior Developer",
          "achievements": ["Hackathon Winner 2024"],
          "activeSince": "2024-01-15"
        },
        {
          "activity": "Music Club",
          "role": "Vocalist",
          "achievements": ["Singer Winner 2024"],
          "activeSince": "2024-10-01"
        }
      ]
    },
    "schoolInfo": {
      "name": "Bright Future Academy",
      "type": "Private International School",
      "established": "2005",
      "accreditation": "CBSE",
      "location": {
        "city": "Bangalore",
        "state": "Karnataka",
        "country": "India",
        "pincode": 123456,
        "coordinates": {
          "latitude": 12.9716,
          "longitude": 77.5946
        }
      },
      "contact": {
        "email": "contact@bfa.edu.in",
        "phone": "+91-8001234567",
        "website": "https://www.bfa.edu.in"
      },
      "facilities": ["Science Labs", "Library", "Sports Complex", "Computer Labs"]
    },
    "countryInfo": {
      "name": "India",
      "capital": "New Delhi",
      "officialLanguage": ["Hindi", "English"],
      "currency": "Indian Rupee (INR)",
      "timezone": "IST (UTC+5:30)",
      "culturalHighlights": ["Diverse festivals like Diwali and Holi", "Rich history in mathematics and science"]
    },
    "metadata": {
      "lastUpdated": "2025-06-07T15:30:00Z",
      "source": "Student Management System"
    }
  }
}

# --------------------------------------------
# 📌 NESTED DATA STRUCTURES 
# --------------------------------------------

# Print the tutor name , Bootcamp.

# Print the student’s name, age, and email from studentProfile.personalInfo.

# Count the number of hobbies in studentProfile.hobbies.

# Add "Photography" to studentProfile.hobbies.

# Remove "Video Games" from studentProfile.hobbies.

# Print the school’s name and facilities from schoolInfo.

# Verify if countryInfo.timezone is "IST (UTC+5:30)".

# Print the student’s nationality from studentProfile.personalInfo.

# List all languages in studentProfile.personalInfo.languages.

# Print the school’s contact email from schoolInfo.contact.

# Check if schoolInfo.accreditation is "CBSE".


# --------------------------------------------
# 📌 Intermediate
# --------------------------------------------

# Update the progress.percentage in academicInfo based on modulesCompleted and totalModules.

# List all modules in academicInfo.grades with a score above 85.

# Append a new grade for "Algorithms" with a score of 87 to academicInfo.grades.

# Calculate the average score from academicInfo.grades.

# Format the student’s address as a single string.

# Delete the coordinates field from schoolInfo.location.

# Update studentProfile.personalInfo.age to 13.

# List all extracurricular activities with their roles from studentProfile.extracurricular.

# Calculate the number of classes missed based on academicInfo.attendance.

# Print all cultural highlights from countryInfo.culturalHighlights.


# --------------------------------------------
# 📌 Advanced
# --------------------------------------------

# Check if the pincode in studentProfile.personalInfo.contact.address matches schoolInfo.location.pincode.

# Add a new extracurricular activity for "Debate Club" with role "Speaker" and activeSince "2025-02-01".

# Count total achievements across all studentProfile.extracurricular activities.

# Find the extracurricular activity with the most recent activeSince date.

# Verify if all activeSince dates in studentProfile.extracurricular are before 2025-06-07.
print("""
PLS LEAVE GAPS

""")

"""
Answers
"""

#--------------------------------------------
# 📌 NESTED DATA STRUCTURES 
# --------------------------------------------

# Print the tutor name , Bootcamp.

# Print the student’s name, age, and email from studentProfile.personalInfo.

# Count the number of hobbies in studentProfile.hobbies.

# Add "Photography" to studentProfile.hobbies.

# Remove "Video Games" from studentProfile.hobbies.

# Print the school’s name and facilities from schoolInfo.

# Verify if countryInfo.timezone is "IST (UTC+5:30)".

# Print the student’s nationality from studentProfile.personalInfo.

# List all languages in studentProfile.personalInfo.languages.

# Print the school’s contact email from schoolInfo.contact.

# Check if schoolInfo.accreditation is "CBSE".

myData= {
  "Tutor": "Arvinder Pal",
  "Mode": "Online",
  "Bootcamp": "Online Python Course",
  "data": {
    "studentProfile": {
      "personalInfo": {
        "name": "Govind Iyer",
        "age": 12,
        "grade": 7,
        "studentId": "STU123456",
        "dateOfBirth": "2012-04-15",
        "nationality": "Indian",
        "languages": ["English", "Hindi", "Kannada"],
        "contact": {
          "email": "govind.sharma@example.com",
          "phone": "+91-9876543210",
          "address": {
            "street": "123 MG Road",
            "city": "Bangalore",
            "state": "Karnataka",
            "country": "India",
            "pincode": 123456
          },
          "emergencyContact": {
            "name": "Smrithi Aparajithan",
            "relationship": "Mother",
            "phone": "+91-9686938909"
          }
        }
      },
      "academicInfo": {
        "course": "Python Programming",
        "enrollmentDate": "2024-09-01",
        "progress": {
          "modulesCompleted": 8,
          "totalModules": 20,
          "percentage": 40.0
        },
        "grades": [
          {"module": "Basics", "score": 85},
          {"module": "Functions", "score": 78},
          {"module": "Data Structures", "score": 92}
        ],
        "attendance": {
          "totalClasses": 50,
          "classesAttended": 48,
          "attendancePercentage": 96.0
        }
      },
      "hobbies": ["Cricket", "Video Games", "Coding", "Music", "Chess","Basketball"],
      "extracurricular": [
        {
          "activity": "Cricket Club",
          "role": "Member",
          "achievements": ["Best Batsman 2024"],
          "activeSince": "2023-06-01"
        },
        {
          "activity": "Coding Club",
          "role": "Junior Developer",
          "achievements": ["Hackathon Winner 2024"],
          "activeSince": "2024-01-15"
        },
        {
          "activity": "Music Club",
          "role": "Vocalist",
          "achievements": ["Singer Winner 2024"],
          "activeSince": "2024-10-01"
        }
      ]
    },
    "schoolInfo": {
      "name": "Bright Future Academy",
      "type": "Private International School",
      "established": "2005",
      "accreditation": "CBSE",
      "location": {
        "city": "Bangalore",
        "state": "Karnataka",
        "country": "India",
        "pincode": 123456,
        "coordinates": {
          "latitude": 12.9716,
          "longitude": 77.5946
        }
      },
      "contact": {
        "email": "contact@bfa.edu.in",
        "phone": "+91-8001234567",
        "website": "https://www.bfa.edu.in"
      },
      "facilities": ["Science Labs", "Library", "Sports Complex", "Computer Labs"]
    },
    "countryInfo": {
      "name": "India",
      "capital": "New Delhi",
      "officialLanguage": ["Hindi", "English"],
      "currency": "Indian Rupee (INR)",
      "timezone": "IST (UTC+5:30)",
      "culturalHighlights": ["Diverse festivals like Diwali and Holi", "Rich history in mathematics and science"]
    },
    "metadata": {
      "lastUpdated": "2025-06-07T15:30:00Z",
      "source": "Student Management System"
    }
  }
}


print("---------------------------------------------Beginner---------------------------------------")

#A1--

print(myData["Tutor"])
print(myData["Bootcamp"])




# #A2--

Dice=myData["data"]["studentProfile"]["personalInfo"]["name"]
print(Dice)
Dice1=myData["data"]["studentProfile"]["personalInfo"]["age"]
print(Dice1)
Dice2=myData["data"]["studentProfile"]["personalInfo"]["contact"]["email"]
print(Dice2)

# #A3--

Duit=myData["data"]["studentProfile"]["hobbies"]
print(len(Duit))

# #4--
# Add "Photography" to studentProfile.hobbies.
myData["data"]["studentProfile"]["hobbies"]
myData["data"]["studentProfile"]["hobbies"].append("photograph")
print(myData["data"]["studentProfile"]["hobbies"])

# #5--
# Remove "Video Games" from studentProfile.hobbies.

myData["data"]["studentProfile"]["hobbies"]
myData["data"]["studentProfile"]["hobbies"].remove("Video Games")
print(myData["data"]["studentProfile"]["hobbies"])

#6--
# Print the school’s name and facilities from schoolInfo.
print(myData["data"]["schoolInfo"]["name"])
print(myData["data"]["schoolInfo"]["facilities"])

#7--
#Verify if countryInfo.timezone is "IST (UTC+5:30)"

print(myData["data"]["countryInfo"]["timezone"])

#8--
# Print the student’s nationality from studentProfile.personalInfo.

print(myData["data"]["studentProfile"]["personalInfo"]["nationality"])

#9--
# List all languages in studentProfile.personalInfo.languages.
print(myData["data"]["studentProfile"]["personalInfo"]["languages"])
#10--
# Print the school’s contact email from schoolInfo.contact.
print(myData["data"]["schoolInfo"]["contact"])
#11-
# Check if schoolInfo.accreditation is "CBSE".
print(myData["data"]["schoolInfo"]["accreditation"])

print("---------------------------Intermediate----------------------")
# Update the progress.percentage in academicInfo based on modulesCompleted and totalModules.

# List all modules in academicInfo.grades with a score above 85.

# Append a new grade for "Algorithms" with a score of 87 to academicInfo.grades.

# Calculate the average score from academicInfo.grades.

# Format the student’s address as a single string.

# Delete the coordinates field from schoolInfo.location.

# Update studentProfile.personalInfo.age to 13.

# List all extracurricular activities with their roles from studentProfile.extracurricular.

# Calculate the number of classes missed based on academicInfo.attendance.

# Print all cultural highlights from countryInfo.culturalHighlights.

#A1--
# Update the progress.percentage in academicInfo based on modulesCompleted and totalModules.

print(myData["data"]["studentProfile"]["academicInfo"]["progress"]["percentage"])

#A2--
# List all modules in academicInfo.grades with a score above 85.

for i in (myData["data"]["studentProfile"]["academicInfo"]["grades"]):
    if i["score"]>=85:
        print(i["score"])
    

       

# print(myData["data"]["studentProfile"]["academicInfo"]["grades"][0]["score"])
# print(myData["data"]["studentProfile"]["academicInfo"]["grades"][1]["score"])
# print(myData["data"]["studentProfile"]["academicInfo"]["grades"][2]["score"])

    






#A3--
# Append a new grade for "Algorithms" with a score of 87 to academicInfo.grades

myData["data"]["studentProfile"]["academicInfo"]["grades"].append({"module": "Algorithms", "score": 87})
print(myData["data"]["studentProfile"]["academicInfo"]["grades"])





#A4--
# Calculate the average score from academicInfo.grades.
co=0
for i in range(len(myData["data"]["studentProfile"]["academicInfo"]["grades"])):
    co+=myData["data"]["studentProfile"]["academicInfo"]["grades"][i]["score"]
print(co/len(myData["data"]["studentProfile"]["academicInfo"]["grades"]))
    
    

    


#A5--
# Format the student’s address as a single string.

# n=""
# for i in range(len(myData["data"]["studentProfile"]["personalInfo"]["contact"]["address"])):
#     n+=myData["data"]["studentProfile"]["personalInfo"]["contact"]["address"]
    
    
#A6--
# Delete the coordinates field from schoolInfo.location.
myData["data"]["schoolInfo"].pop("location")
print(myData["data"]["schoolInfo"])


#A7--
# Update studentProfile.personalInfo.age to 13.

myData["data"]["studentProfile"]["personalInfo"]["age"]=13
print(myData["data"]["studentProfile"]["personalInfo"]["age"])

#A8--
# List all extracurricular activities with their roles from studentProfile.extracurricular.

# B=myData.values(["data"]["studentProfile"]["extracurricular"]["role"])
# print(B)


#A9--
# Calculate the number of classes missed based on academicInfo.attendance.
A=myData["data"]["studentProfile"]["academicInfo"]["attendance"]["totalClasses"]-myData["data"]["studentProfile"]["academicInfo"]["attendance"]["classesAttended"]
print(A,"Missed Classes")


#A10--
# Print all cultural highlights from countryInfo.culturalHighlights.
print(myData["data"]["countryInfo"]["culturalHighlights"])


print("--------------------------Advanced-----------------------")
# Check if the pincode in studentProfile.personalInfo.contact.address matches schoolInfo.location.pincode.

# Add a new extracurricular activity for "Debate Club" with role "Speaker" and activeSince "2025-02-01".

# Count total achievements across all studentProfile.extracurricular activities.

# Find the extracurricular activity with the most recent activeSince date.

# Verify if all activeSince dates in studentProfile.extracurricular are before 2025-06-07.
#A1--
for i in myData["data"]["studentProfile"]["personalInfo"]["contact"]["address"]:
    if i in myData["data"]["schoolInfo"]["location"]["pincode"]:
        print(True)
    else:
        print(False)