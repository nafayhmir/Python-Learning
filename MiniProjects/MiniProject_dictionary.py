students = {
    "24K-1234": {
        "name": "Ali",
        "age": 20,
        "department": "EE",
        "semester": 3,
        "cgpa": 3.45,
        "courses": ["MVC", "ENA"],
        "attendance": 92,
        "phone": "03001234567"
    },
    "24K-1235": {
        "name": "Sara",
        "age": 21,
        "department": "CS",
        "semester": 2,
        "cgpa": 3.82,
        "courses": ["PF", "Calculus"],
        "attendance": 88,
        "phone": "03111234567"
    }
}

def menu():
    print("  Main Menu   ")
    print("1.Display Student")
    print("2.Add Student")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Add Course")
    print("7.Remove Course")
    print("8.Show Highest GPA")
    print("9.Statistics")
    print("10.Exit")
    print()

def display():
    for student_id, information in students.items():
        print("Student ID :", student_id)
        print("Name       :", information["name"])
        print("Age        :", information["age"])
        print("Department :", information["department"])
        print("Semester   :", information["semester"])
        print("CGPA       :", information["cgpa"])
        print("Courses    :", information["courses"])
        print("Attendance :", information["attendance"])
        print("Phone      :", information["phone"])
        print()
        
def add():
    id=int(input("Student ID:"))
    name=input("Name:")
    
menu()
x=int(input("Enter Choice: "))    
if x==1:
    display()
elif x==2:
    add()