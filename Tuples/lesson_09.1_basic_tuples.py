#Basic Tuples
numbers=(1,2,3)#<- this is called a tuple, only visual difference is []->()
#Tuples: Ordered, immutable collection of items.
#Ordered means that indexing still works here.
print(numbers)
print(numbers[0])#Answer should be 2 
print(numbers[-1]) #end of tuple
print(numbers[-2])
# Tuples can also store different variable types
numbers=("ali",2,8.5)
print(numbers)
print(numbers[0]) # Answer should be 2 
print(numbers[-1]) #end of tuple
print(numbers[-2])

#numbers[1]=22 #Tuples cannot be changed like this
#Tuples should be used when you want permanent data stored i.e DOB,Coordinates etc.
empty=()
print(type(empty))  #Function used to identify type of output/input

x1=(5)
x2=("Ali")
print(type(x1))
print(type(x2))
#both of these are normal data types
x3=(5,)
print(type(x3))
#x3 is a tuple due to the presence of ,
x3_2= 5 , #also a tuple
print(type(x3_2))

#nested tuples
x4=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
print(x4,"      ",x4[1])
print(x4[1][1]) #same like nested lists
