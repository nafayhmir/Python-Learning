#Deleting from Dictionaries
student={
    "Name":"Ali",
    "Age":20,
    "CGPA":3.2,
    "Degree":"EE"
}
#Deleting Key-Value pair using del
#del dictionary_name[Key_name]

print(student)
del student["CGPA"] #Deletes both key and value
print(student)

#Deleting using pop
#pop returns the deleted value meaning it can be stored
#Syntax dictionary_name.pop(Key_name)
deg=student.pop("Degree")
print(deg)

#Pop also accepts default
b=student.pop("Car","Not found") #This gives the value to b instead of error
print(b)

#To clear entire dictionary
student.clear()
print(student)
#We can also delete nested dictionaries
S2={
    "Name":"Hamza",
    "Age":22,
    "Marks":{
        "Math":78,
        "Physics":92
    }
}
print(S2)
del S2["Marks"]["Math"]
print(S2)