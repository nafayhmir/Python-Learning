#Nested Lists
#For loop
#Syntax: for variable in list:
    # code
index=0    
numbers=[1,2,3,4,5]
for index in numbers:
    print(numbers) #Will Print entire list highest index times so in this case 5 times

for num in numbers:
    print(num) #Prints each member individually 
    
fruit=["Apple","Banana","Orange"]
for fruit1 in fruit: #Each member of list fruit is stored in variable fruit1
    print(fruit1)

#We can assign value to variable asw    
"""for num in numbers:
    num=100
    print(num)"""

#if we want to change list by loop

for i in range(len(numbers)):
    numbers[i]+=2
    i+=1
    print(num)

print(numbers)    

#range(len) basically helps us to get length and set indexes
#we can also use enumerate function learned in lesson 08.8

#practice: sum of updated Numbers
num1=0
for num in numbers:
    num1+=num    
print(num1)

#Practice Counting a value above 30
data=[10,22,33,44,13,32,94,93,21,44,20,38,30,55]
num2=0
for num3 in data:
    if num3>=30:
        num2=num2+num3
    
print(num2)    