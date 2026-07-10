#List Splicing
#list_name*[start:stop], where start and stop index are'nt included
'''L1=[1,2,3,4,5,6,7,8,9,10]
print(L1[1:6])
print(L1[0:6])
print(L1[:6])
print(L1[0:])
#Slicing returns a List
print(L1[1]) #This Returns back a Value


#Step in between slicing
#list[start:stop:step]-Syntax,step tells how many places to skip, default is 1
print(L1[0::2])# Will Print Odd Numbers as starts from First Index,runs till last element and skips every other entry
print(L1[0::3])#Will print every third copy
#We can also reverse the list
print(L1[::-1])#This means it will start from end (-1 Position) and move back till it reaches length of list
'''
#Practice: Print all members except first 2, and print in intervals of three
L2=[1,2,3,4,5,6,7,8,9,10,"A","B","C","D"]
print(L2[2:])
L3=(L2[2::3]) #Makes a New List, and adds its members to L3, A subset of L2
print(L3)