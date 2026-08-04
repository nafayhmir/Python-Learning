#Why we need nested dictionaries?
#To better organize data
#There is no limit to nested dictionaries

scores={
    "Ali":{
       "Math":75,
       "English":72},
    "Sara":{
        "Math":82,
        "English":88}
}
#Accessing nested values
print(scores["Ali"]["Math"])
print()
#Better practice
print(scores.get("Ali").get("Math")) #Device gets ali and then finds math in Ali's scores

#Adding Nested Keys and values
scores["Ali"]["Chemistry"]=88 #added into ali with key chemistry
print(scores["Ali"]["Chemistry"])
scores["Hamza"]={
    "Math":87,
    "English":85
}
print(scores)

#Deleting a field
del scores["Ali"]["Chemistry"]