# Q18.
# Write a function to update student details based on ID. The function should allow updating name, marks, or both.

students = {
1: {"name": "Rahul", "marks": 80},
2: {"name": "Priya", "marks": 65},
3: {"name": "Amit", "marks": 90}
}

def update_students(students):
    s_id=int(input("enter student ID : "))

    if s_id not in students:
        print("ID is not in student ")

    else:
        print("what dou you want to update")
        print("1.update name")
        print("2.update marks")
        print("3.update both")

        choice=int(input("enter your choice"))

        if choice==1:
            n_name=input("enter new name : ")
            students[s_id]["name"]=n_name

        elif choice==2:
            n_marks=input("enter new marks : ")
            students[s_id]["marks"]=n_marks

        elif choice==3:
             n_name=input("enter new name : ")
             n_marks=input("enter new marks : ")
             students[s_id]["name"]=n_name
             students[s_id]["marks"]=n_marks
        else:
            print("Invalid choice")
            return

        print("students details updated successfully")     

update_students(students) 
print("updated dictionary")
print(students)  
 



   
        

