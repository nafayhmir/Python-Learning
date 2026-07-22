#Creating Dictionaries
'''
General Syntax:
dict_name{
    "key1":value1,
    "key2":value2,
    "key3":value3
}
'''
#colons connect key with value
#Empty Dictionaries
dicti={}
#dictionaries can store different variable types
phone_speck={
    "Name":"Python",
    "Price":2000
}
#Keys dont need to be only strings
data={
    1:20,
    3.14:10,
    (2,3):5
}
print(data[(2,3)]) #cannot be lists as they can be changed
#Values can be duplicates, but keys wont
s1={
    "Name":"Ali",
    "Name":"Ahmed"
}
marks={
    "Sara":90,
    "Ali":90    
}
print(s1["Name"]) #Will overwrite value to most recent value
print(marks["Ali"],marks["Sara"]) #this works

#Nested dictionaries
s2={
    "Name":"Ali",
    "Marks":{
        "Math":88,
        "English":90
    }
}
print(s2["Marks"])

#Creating Dictionaries with dict()
#instead of {} we can use dict()
#Syntax
"""
dictionaries_name=dict(
    key=value
)
"""
grades=dict(
    Ali=77, #converts automatically to python string
    Mir=65
)
print(grades)

data = [
    ("name","Ali"),
    ("age",20),
    ("cgpa",3.5)
]
student=dict(data)
print(student)

#We can also create 2 separate tuples of keys and values respectively and merge them while making dic
keys = ("name","age","cgpa")
values = ("Ali",20,3.8)
student=dict(zip(keys,values)) #Making a dict with name student,by merging keys and values using zip
#here keys must be equal to values to make this work

#we can also assign same value to each key 
subject=("Math","english","CS")
marks=dict.fromkeys(subject,10)  #We make a dict from keys stored in subject and give value of 10 to each
print(marks)
#Always Remember from keys always give same value to each key regardless if we tell it to assign it to specific key
