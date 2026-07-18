#1: Print Every Element
numbers = [12, 25, 18, 40, 9, 27, 88, 98]
print(numbers)
#print with index number
index=0
for index,row in enumerate(numbers):
    print(index,":",row)
    
#print even numbers
for row in numbers:
    if row%2==0:
        print(row)

#Create a new list with squares
index=0
squares=[]
for row in numbers:
    squares.append(row*row) #List need append function to be edited 

print(squares)

#Find sum and max number without built in functions
#Sum
sum=0
for row in numbers:
    sum+=row

print("Sum:",sum)

#Max
max=numbers[0]

for row in numbers:
    if row>max:
        max=row
    
    
print("Max:",max)

#Check Whether specific number exists in list

print("Exists:",9 in numbers)

#Seperate Even and odd numbers
even=[]
odd=[]
for row in numbers:
    if row%2==0:
        even.append(row)
    else:
        odd.append(row)
        
    
print(odd)
print(even)

#Print Index where 9 exists
index=0
for row in numbers:
    if row == 9:
        print(index)
    index+=1