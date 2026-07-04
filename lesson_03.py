#Even and Odd Check
'''x=int(input("Input Number: "))
y=x%2
if y==0:
    print("Even Number")
else:
    print("Odd Number")'''
    
#Positive,Negative and Zero check
'''x=int(input("Input Number: "))
if x>0:
    print("Positive Number")
elif x==0:
    print("Number is Zero")
elif x<0:
    print("Number is Negative")'''

#Password Check
'''x=input("Password: ")
if x=="N11":
    print("Same Password") #String Check
else:
    print("Password is Wrong")'''

#Grade Calculator
'''x=int(input("Input Marks: "))
if x>90:
    print("A+")
elif x>80 and x<90:
    print("A")
elif x>70 and x<80:
    print("B")
elif x>60 and x<70:
    print("C")'''

#Basic Atm Menu
x=100000
print("1-Balance Check")
print("2-Deposit")
print("3-Withdraw")
print("4-Exit")
y=int(input(" Choice: "))
if y==1:
    print(x)
elif y==2:
    a=int(input("How much you want to Deposit?"))    
    x=x+a
    print("New Balance:",x)
elif y==3:
    b=int(input("How much you want to withdraw?"))
    x=x-b
    print("New Balance:",x)
