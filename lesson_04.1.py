#Loops
#For Loop:
#Password checker
'''
print("Welcome To Password check")
x="Pass123"

for i in range(3): #range(start(included in iterations),stop(not included))
    y=input("Enter Password:")
    if y==x:
        print("Password is Correct")
    else:
        print("Password is Wrong, Try again")
'''

#using step in range
'''for i in range(0,11,2):#(third argument for telling how many iterations to skip)
    print(i)'''

#counting backwards
'''for i in range(10,0,-1):
    print(i)'''

#Practice task Table of 2
'''a=2
for i in range(1,11):
    print(a,"x",i,"=",a*i'''
    
#Practice Task Sum of Numbers
x=int(input("Enter a Sum of required Numbers(from 0):"))
a=0
for i in range(0,x):
    a=a+i
print("Sum=",a)