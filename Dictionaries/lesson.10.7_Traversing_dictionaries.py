#Traversal in Dictionaries
student = {
    "Name": "Ali",
    "Age": 20,
    "CGPA": 3.8
}

#To check keys only we can use keyword key
for key in student: #Key is the keyword
    print(key)
print()
#to only check values we use traverse through values only
for value in student.values():
    print(value)    
print()    

#to get keys and values for each 
for key in student:
    print(key,":",student[key]) #we are printing value of key in student #Returns String
#or
for item in student.items():
    print(item) #returns tuples
    
#To traverse nested dictionaries
students = {
    "Ali": {
        "Math": 90,
        "Physics": 80
    },
    "Sara": {
        "Math": 95,
        "Physics": 88
    }
}
for student,marks in students.items():
    print(student)
    for subject,score in marks.items():
        print(subject,score)

#Basically this says that for each student print the name and then print each subject and score in marks.items
#When traversing through dictionaries we cant change space of dictionary but can edit it
scores={
    "Math":88,
    "Eng":78,
    "Chem":86
}
for student in scores:
    scores[student]+=5

print(scores)
#we cant add or remove keys