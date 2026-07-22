students = [
    ["Ali", 80],
    ["Sara", 92],
    ["Ahmed", 67]
]

def display():
    i1=0
    print("Students","Marks")
    for row in students:
        print(row[0],row[1])
        
        
def add(name,marks):
    students.extend([name,marks])

def Search(name):
    for row in students:
        for col in row:
            if col==name:
                print(row)
                break
            
def update(name,new_marks):
    for row in students:
        for col in row:
            if col == name:
                students[row][col]=new_marks
                print(students)     
            
def delete(name):
    for row in students:
        for col in row:
            if col==name:
                del students[row]
                
def stats():
    sum=0
    avg=0.0
    index=1
    for row in students:
        sum+=row[1]
        avg+=row[1]
    
    avg=avg/len(students)
    print("Sum of all Marks:",sum)
    print("Average Marks", avg) 
    print("Highest Marks:",max(students))   
        
        
while True:

    print("========================================")
    print("MAIN MENU   ")
    print("Student Management System   ")
    print("1.Display Students")
    print("2.Add Student")
    print("3.Search Student")
    print("4.Update Marks")
    print("5.Delete Student")
    print("6.Statistics")
    print("0.Exit")
    
    x=int(input("Numbered Option:"))
    if x==1:
        display()
    if x==2:
        a=(input("Name:"))
        b=int(input("Marks:"))
        add(a,b)
    if x==3:
        c=input("Name To find: ")
        Search(c)
    if x==4:
        d=input("Name of Student to change marks:")
        e=int(input("New Marks:"))
        update(d,e)
    if x==5:
        f=input("Students Name to delete: ")   
        delete(f) 
        print(students)
    if x==6:
        stats()
    if x==0:
        break
    