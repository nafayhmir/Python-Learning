#Creating Tuples
#We can turn lists into tuples using tuples constructor
l=[1,2,3,4,5,6,7]
print(l)#output with []
t=tuple(l)
print(t) #output with ()
#We can also turn strings,int to tuples
l2="Python"
t2=tuple(l2)
print(t2)

#we can also convert tuple to list using list constructor
l3=list(t) #back to []
print(l3)
l4=list(t2) #back to []
print(l4)

#To make changes into tuples we using this workflow
#Tuple->list->modify list->tuple
