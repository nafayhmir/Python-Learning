#Built in Methods and Functions
student={
    "Name":"Ali",
    "Age":20,
    "CGPA":3.5,
    "Marks":{
        "Math":88,
        "English":75
    }
}
#Method1
print(student.keys()) #Prints All keys in dictionary
print(student.values()) #prints all values
print(student.items()) #Prints all keys and 
s2=student #Both point to same dictionary so any change in s2 will affect student
s3=student.copy() #Copy's dictionary
print(s3)
