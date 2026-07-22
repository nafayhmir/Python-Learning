#Using Tuples
#we can use the index of tuples to display info only as they cant be modified

t=(10,8,9,7,6,5,4,3,2)
print(t) #Print entire Tuple
print(t[0]) #prints First Index
print(t[-len(t)]) #print first index using negative indexing
print(t[-1]) #prints last element in tuple

#We can also incorporate slicing 
print(t[0:4]) #Prints first 4 index including 0th index but excluding 4th index
#we can also create new tuples using slicing
t1=t[:4] #Will start from beginning and end before index 4 so 0,1,2,3 will be included
t2=t[4:] #Will start from fourth index and copy till last index

#We can also incorporate step in it
t3=t[::2] #Will start from beginning and end at last index but leave every other index

#We can also use a loop to represent members of tuple
for ts in t:
    print(ts)
print()
for i in range(len(t)):
    print(i,t[i]) # Gives index number as well
    
#We can also use membership operators on tuples
print(8 in t) #Checks if number 8 is in tuple
print(8 in t2)

#Practice
students=(
    ("Ali",90),
    ("Sara",82),
    ("Mir",98)
)
#Print Student_name scored marks

for student in students:
    print(student[0],"scored",student[1])