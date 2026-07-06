#Nested Loops

#Multiplication Tables
'''for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t") #Property of print function, automatically ends with an new line so end="\t"
        #helps with maintaining looks
    print()#used to separate outputs into lines'''
    
#Outer loops controls Rows, inner loop controls column

#Rectangle
'''for row in range(4): 
    for col in range(6):
        print("*", end=" ")
    print()   '''

#Practice (Make a 5*5 star square)

'''for row in range(5):
    for col in range(5):
        print("*",end=" ")
    print()    '''

#Practice (Print the same square but with numbers)
'''for row in  range(5):
    for col in range(5):
        print(col,end="")
    print()    '''
    
#Practice (User Based Multiplication tables)    
x=int(input("Which Multiplication table do you require? "))
y=int(input("Till where should this table go? "))
x=x+1
y=y+1
for row in range(1,x):
    for col in range(1,y):
        print(row,"x",col,"=",row*col)
    print()
    
    
    