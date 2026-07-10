#Methods-2
l=["A","B","C","D","E"]
print("Original: ",l)

#Method 1: Clear; clears all members of a object
l.clear()
print("Cleared: ",l)
#object will exist but will be empty

#Method 2: index; used to find index of a specific value
l1=[1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
print("New: ",l1)
x=l1.index(8)
print("Index of Value 8 is",x)
#if repetitions are there so it will give index of first occurrence 

#Method 3: count; used to count repetitions
y=l1.count(2)
print("Repetitions of 2 are ",y)

#Methods 4: Sort; Used to sort components of object
#Ascending Order is default
l1.sort()
print("Ascended Sort:",l1)

#Descending Syntax: list_name.sort(reverse=True)
l1.sort(reverse=True)
print("Descending Order:",l1)
#For strings Python will sort based on Alphabets so A will always come first, and capital words will be stored before
l2=["A","a","B","b","D"]
print("Alphabet List: ",l2)
l2.sort()
print("Sorted Alphabets List: ",l2)
#Python cannot sort multiple data types together

#Method 4: Reverse; Reverses the entire list
l3=[1,0,1,0,1,0,1,0,1,0,1,0]
print("Third List:",l3)
l3.reverse()
print("Reversed List:",l3)

#Method 5: copy;creates a new list with all copied material and any changes to new list wont affect other
a = [1,2,3]
b = a.copy()
b.append(4)
print(a)
print(b)

#will be covered in depth later
