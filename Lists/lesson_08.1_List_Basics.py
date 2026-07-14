#Lists Fundamentals
#Basically Like Arrays but are able to store different data types
#i.e students = ["Ali", "Ahmed", "Sara", "Fatima"]
#we can access these lists using [index_no],index starts from 0
'''students = ["Ali", "Ahmed", "Sara", "Fatima"]
print(students)
print(students[2])
#Python will remember the order that the items were placed in
#We can also edit individual parts of the List
students[1]="Nafayh"
print(students)'''
#Duplicates are possible and we dont need to specify size of list

#Empty lists
empty=[]
print(empty)
#Lists can store multiple types of values
list_1=[True,3.22,3,"Car"]
print(list_1)

#Memory in lists:
#Memory is alloted to each variable instead of each component

#Practice, Representing a Nested List for a 2*2 Matrix
a=int(input("First Member: "))
b=int(input("Second Member: "))
c=int(input("Third Member: "))
d=int(input("Fourth Member: "))
matrix=[
    [a, b],
    [c, d]
]
print(matrix)