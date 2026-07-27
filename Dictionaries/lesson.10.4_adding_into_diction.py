#Adding and Updating Dictionaries
student={
    "Name":"Ali",
    "Age":20,
    "Marks":{
        "Math":88,
        "English":76
    }
}

#Adding into existing dictionary
#syntax: dictionary_name[New_key]=value
student["Department"]="Electrical Engineering"
print(student.keys())

#we can update existing values of keys 
#Syntax is same as Adding into library
student["Age"]=21
print(student.values())
#To Update nested Dictionaries
student["Marks"]["Math"]=87
print(student)
#we can also add a new key for marks by
student["Marks"]["Chemistry"]=78
print(student)
#we can also update more than one key using .update()
student.update({
    "Age":22,
    "GPA":3.8
})
print(student)

#we can Merge 2 Separate dictionaries using.update()
s_residence={
    "House":1741,
    "City":"Karachi"
}
student.update(s_residence) #dict_to_store.update(dictionary to merge)
print(student)
