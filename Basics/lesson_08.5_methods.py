#Methods
#Methods are function run on objects, example of objects include
fruit=["Apple","Banana","Mango"]
print("Original:",fruit)

#Method 1: Append; Adds input to the end of object
fruit.append("Orange")#Can only add one thing
print("Appended: ",fruit)

#Method 2: Extend; Adds multiple inputs at end of object
fruit.extend(["Kiwi","Watermelon"]) #Takes one input but if input is in [] then it automatically removes brackets
print("Extended: ",fruit)

#Method 3: Insert; Inserts at a specific index and moves the rest forward
fruit.insert(0,"Apple") #.insert(index,object to add)
print("Inserted: ",fruit)

#Method 4: Remove; Removes first Occurrence 
fruit.remove("Apple")
print("Removed: ",fruit)

#Method 5: Pop: It removes from index and can be used to store the removed data
x=fruit.pop(0)
print("Popped: ",fruit)
print("Value of Removed: ",x)

