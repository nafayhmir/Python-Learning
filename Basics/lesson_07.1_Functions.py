#Functions
#Syntax
#def function_name(parameters):               Def means defining a new function
#function body
#A function can have multiple parameters

#Practice 1: Greeting function
'''
def say_hello(name):
    print("Hello",name)
    

say_hello("Nafayh")'''

#Practice 2: Square Number
'''def sqrt(x):
    x=x*x
    print(x)
    
sqrt(8)'''

#Practice 3: Area of Triangle
'''def area(base,height):
    Area=0.5*base*height
    print(Area)

area(10,10)'''

#Practice 4: Calculator
def add(a,b):
    x=a+b
    print(x)

def sub(a,b):
    x=a-b
    print(x)
    
def mul(a,b):
    x=a*b
    print(x)
    
def divide(a,b):
    x=a/b
    print(x)
    
x=int(input("First Number: "))
y=int(input("Second Number: "))
z=input("Sign of what you want todo(+,-,*,/): ")

if z=="+":
    add(x,y)
elif z=="-":
    sub(x,y)
elif z=="*":    
    mul(x,y)
elif z=="/":
    divide(x,y)