#Updating and Adding to Lists
#We can update lists using mutation we learned in 8.1 or if we need to update multiple values
l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)
l1[5:7]=[2,2]
print(l1)
#we can also reduce length of the list using the same command
l1[5:7]=[1]
print(l1)

#Adding to PreExisting Lists
#to add something to a list we use the help of append method
#syntax: list_name.append(what you want to add), it will be added in the last of existing list
l1.append(99)
print(l1)
#we can also add using concatenation
l2=[1,2,3,4,5,6]
l3=l1+l2
print(l3)

#Removing List Members
#we can remove specific members of a list using del keyword
del(l3[0]) #Removed the first member of the list
print(l3)
#if we use del function and not add any arguments then it will delete list aswell 