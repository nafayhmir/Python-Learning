#String Operations
#general syntax string_name.method()

#method 1:Upper
#Converts every Letter to Upper case
'''text = "fast university"
print(text.upper())'''

#Method 2: Lower
#Converts every letter to lower case
'''text="FAST UNIVERSITY"
print(text.lower())'''

#Method 3: Title
#Capitalizes First letter of each word
'''text="nafayh akhlaq ahmed"
print(text.title())'''

#Method 4: Capitalize
#Capitalizes first letter only
'''name="Nafayh Akhlaq"
print(name.capitalize())'''

#Method 5: Strip
#Removes whitespaces from both sides of variable
'''x="       x         "
print(x.strip())'''
#lstrip removes whitespace from left and rstrip removes from right

#Method 6: Replace
#Replaces one part of string with another
'''text="Hello World"
print(text.replace("World","Nafayh")) #replace(what you want to replace,what you want to replace with)'''

#Method 7: Find
#Finds a specific letter or word and returns first index of that word
'''text="Hello World, This is Nafayh Coding this."
print(text.find("o"))
print(text.find("."))'''
#If it cannot find something it will return a value of -1

#Method 8: Count
#Counts number of times a word or letter is repeated
'''text="A car is going down the highway"
print(text.count("o"))'''

#Method 9: Startswith and endswith
#Checks prefix and suffix if it matches, returns True if it matches
'''text="Pakistan"
print(text.startswith("P"))
print(text.endswith("an"))'''

#Method 10: Split 
#Splits string into separate strings
'''text="Python is awesome"
print(text.split())
x=text.split()'''

#Method 11: Joining
#Joins separated string into one.
#Syntax:
#print("what you want to separate with".join(where split up string is))
'''print(" ".join(x))'''

#Practice Task: Password Generator (8 Characters,One uppercase,lowercase and number each)
x=input("Please Validate Password: ")
length=len(x)
split=x.split()
uppercase=False
lowercase=False
number=False
i=0
if length>=7:
    for i in range(7):
        if x[i].islower():
            lowercase=True
        elif x[i].isupper():
            uppercase=True
        elif x[i].isdigit():
            number=True


if number==True and uppercase==True and lowercase==True:
    print("Correct Password")
else:
    print("Wrong Password")