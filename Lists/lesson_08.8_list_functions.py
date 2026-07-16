#basic Syntax: function(object) instead of object.method
#1 len()->Gives the length
numbers=[10,9,8,7,6,5,4,3,2,1]
data=[1,2,[9,8],5]
letters=[" A","B","C","a","b"]
floats=[0.5,1.5,3.75]
print("Length:",len(numbers))
print("Length of Data:",len(data))

#min()->Returns Smallest number
print("Minimum Value",min(numbers))
print("Minimum Value in letters",min(letters)) #Based on ASCII values

#min()->Returns Largest Value
print("Maximum Value",max(numbers))
print("Maximum Value in letters",max(letters))#Based On ASCII Values
print("Maximum Value in Floats",max(floats))

#sum()-> Returns sum
print("Sum of Numbers:",sum(numbers))
print("Sum Of Floats:",sum(floats))

#sorted()->Creates a new list of sorted elements
num2=sorted(numbers)
print("Unsorted Numbers:",numbers) #can also be written as list,reverse=true
print("Sorted Numbers:",num2)

#enumerate() -> Assigns index numbers to each list members, requires loop
index=0
for index,numbers in enumerate(numbers):
    print(index,numbers)
    
#zip()-> combines two separate lists
Name=["Ali","Ahmed","Rayan"]

for Name, letters in zip(Name,letters):
    print(Name,letters)

#list()->Converts Input to list
word="Python"
list1=list(word)
print(list1)