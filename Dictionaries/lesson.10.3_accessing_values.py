#Accessing Values
student ={
    "name": "Ali",
    "age": 20,
    "department": "EE",
    "GPA":3.2,
    "Marks":{
        "English":71,
        "Math":88,
        
    }
}

#Method 1: Using []
print(student["name"])
#we can use this to print all details with spaces like
print(student["name"],student["age"],student["department"],student["GPA"])
#If we search for a non existent word, we get a error
#print(student["name"],student["age"],student["department"],student["GPA"],student["Car"]) #key Car doesn't exist so we get a Key error
#python is case sensitive so Age is not same as age

#Method 2: Using .get()
#Syntax: dictionary.get(Key)
print(student.get("name")) 
#if we input a key that doesn't exist or different case word it wont give error it will only show None
print(student.get("Name"))
#using get also helps us due to its second argument
#dictionary.get(key,Default Value)->we can give a default value if there is no value to that key

#Deriving from nested dictionaries
print(student["Marks"]["Math"]) #Same as lists or tuples
print(student.get("Marks").get("Math"))
#Like printing we can also assign all these values to variables as well

#We can also use membership operators but they will only check if key exists
print("name" in student)
print("Name" in student)
#We can check if a key/value certain exists 
print("Ali" in student.values()) #Will check values for Ali
print("department" in student.keys()) #Will check keys for department

#.keys(),.values(),.items()
#.keys() display all keys in dictionary
print(student.keys())
#.values() displays all values in dictionary
print(student.values())
#.items() displays both keys and values
print(student.items())