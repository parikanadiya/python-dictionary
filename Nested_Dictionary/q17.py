# Q17.
# Write a function to add a new student record. Make sure duplicate IDs are not allowed.

students = {
1: {"name": "Rahul", "marks": 80},
2: {"name": "Priya", "marks": 65},
3: {"name": "Amit", "marks": 90}
}

def add_students(students):
    s_id=int(input("enter student ID"))

    if s_id in students:
        print("duplicate id is not allowed ")
        return
    
    name=input("enter name : ")
    marks=int(input("enter marks : "))

    students[s_id]={
        "name":name,
        "marks":marks
    }

    print("student added successfully")

add_students(students)
print(students)
