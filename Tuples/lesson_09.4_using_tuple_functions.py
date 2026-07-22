#Tuple Functions
#Due to being unchangeable only 2 methods work for tuple, count and index
#Methods
t=(1,2,3,4,5,6,7,8,9,2,3,2,2,3,-1)
t1=("Ali","Ahmed","Ali")
print(t.count(2))#tells number of repetitions of where value is stored
print(t.index(1)) #Gives index of first occurrence of 1
print(t1.count("Ali"))

#Functions
#len()->Length of tuple
print(len(t))

#max()-> Maximum value in tuple
print(max(t))
print(max(t1))

#min()-> Minimum value in tuple
print(min(t))

#sum()-> Sum of all values in tuple, only works for numbers
print(sum(t))

#sorted()-> Sorts the tuple but does not change it
print(sorted(t))
t2=sorted(t)
print(t2)
#sorting gives us a list and not tuple, which means sorted tuples can be changed

#Reverse()-> Reverses tuple
print(tuple(reversed(t))) # Need to tell it to return a tuple and not list else it wont work
t3=reversed(t)

#Operators
T1=(1,2,3)
T2=(4,5,6)
print(T1+T2) #Concatenation 
print(T1*2) #Repetition of same Tuple
print(T1==T2) #Check each index of both and compares
print(T1<T2) #Check each index of both and compares
print(T1>T2) #Check each index of both and compares

#Packaging and Unpacking
Student="Ali",19,3.4 # Python will automatically package this into a tuple
name,age,gpa=Student #Automatically assigns each variable with a value from student
print(age)

#Practice
'''
Use extended unpacking on:
numbers = (10, 20, 30, 40, 50, 60)
so the first and last values go into separate variables and everything in between is collected by middle.
'''
numbers =10, 20, 30, 40, 50, 60
first,*middle,end=numbers
print(middle) #If you want to store values in between start and end use * 