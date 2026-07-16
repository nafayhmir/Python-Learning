#List Operators
#"+":Concatenation
#Combines two separate list into a new list
a=["A","B","C"]
b=[1,2,3]
c=a+b
print("Concatenation:",c)

#"*": Repetition
#Syntax: print(list_name * number of times you want to print)
print("Repetition:",a*3)

#"in and "not in": Membership Operators
#Returns True or False
#Syntax: print("word to find" in list_name)
print("Membership:","A" in a)
print("Membership:",3 not in b)
#For numbers dont use ""

#Comparison Operators
#1) "==": Are lists equal?
#2) "!=": Are lists not equal?
print("Is List A and B equal?",a==b)

#Less than,greater than
#For Lists Python compares element by element
d=[1,2,3,4,5]
e=[5,4,3,2,1]
print(d<e)#at least 1 element satisfies so it works
#smaller list is considered smaller value so [1,2]<[1,2,3]
print([5,1]<[2,7]) #will check till condition is satisfied

#Assignment Operator
num=[1,2]
print(num)
num+=[3,4]
print(num)

#Repetition Operator
num=[1,2]
num *=3 #Easier way to write "*"
print(num)

#"is" : Checks both value and memory
a = [1,2,3]
b = [1,2,3]
print(a is b)
