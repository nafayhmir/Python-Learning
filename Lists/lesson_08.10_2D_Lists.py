#2D Lists
#Nested List is basically a list with lists as its elements i.e
marks=[["Ali",10],
       ["Ahmed",8],
       ["Rayan",9]]
#When accessing 0 index we will get both members of the element
print(marks[0])
#To access indivual member of list we need to give the index two times
#Forexample to access Ali's marks we need 
print(marks[0][1]) #[Row][Col]

#to change marks of a member i.e Rayan's marks to 10
print("Original Marks:",marks[2])
marks[2][1]=10
print("New Marks:",marks[2])

#Looping through 2d Lists
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
#The below code will print each row separately in a matrix form
for row in matrix:
    print(row)
    
#To print each member on a separate row we will use 2 loops
for row in matrix:
    for col in row: #the Second loop is connected to variable of first loop
        print(col)

#To Print in True Matrix style        
for row in matrix:
    for col in row: #the Second loop is connected to variable of first loop
        print(col,end=" ") #Each Column will have a block of space in btw
    print() #line in between each row    
        

#Practice: Find sum of matrix
sum=0
for row in matrix:
    for col in row:
        sum=sum+col 
               
print(sum)

#Jagged Lists
matrix2=[
    [1,2],
    [2],
    ]

for row in matrix2:
    print(row)
     