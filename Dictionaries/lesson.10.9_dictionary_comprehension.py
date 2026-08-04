#Dictionary Comprehension
#Syntax
#dictionary={
    #key:value
    #for something in iterable 
#}

#example
numbers=[1,2,3,4,5]
square={
    number:number**2
    for number in numbers
}
print(square)
#example 2
names=["Ali","Sara","Ammar"]
students={
    name:len(names)
    for name in names
    }
'''
basically this makes it easier to add keys and values into a empty or non empty dictionary
'''
#example 3
numbers=[2,4,6,8,10]
mult={
    numbers:numbers*10
    for numbers in numbers
}
print(mult)

#example 4:using if
num1=[1,2,3,4,5,6,7,8,9,10]
cube={
    num1:num1**3
    for num1 in num1
    if num1%2==0 #giving condition in dictionary
}
print(cube)
