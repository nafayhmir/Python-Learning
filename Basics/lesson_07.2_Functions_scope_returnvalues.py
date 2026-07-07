#Scope and Return Values
#Return Value
#use return when defining a function so you dont have to print like previously i.e
'''
def add(a,b):
    x=a+b
    return x

a=5
b=10
c=add(a,b)
print(c)'''
#We can basically store values of functions using return

#we can also return multiple values
'''def calculate(a, b):
    return a + b, a - b

sum_result, difference = calculate(10, 4)

print(sum_result)
print(difference)'''

#Practice: Student Grade Calculator 
def grade(num):
    if num>90:
        return "A+"
    elif num>80:
        return "A"
    elif num>70:
        return "B"
    elif num>60:
        return "C"
    elif num>50:
        return "D"
    elif num<50:
        return "F"
    
print("Grade",grade(88))