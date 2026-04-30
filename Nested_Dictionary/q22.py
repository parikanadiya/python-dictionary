# Q22.
# Write a program to search for a student by name and display their details

students={
    1:{"name":"pari","marks":67},
    2: {"name": "Priya", "marks": 65},
    3: {"name": "Amit", "marks": 90}

}

search=input("enter name of student you want to found : ")

for s_id,data in students.items():
    if data["name"].lower()==search.lower():
        print("student found")
        print("ID : ",s_id)
        print("Name : ",data["name"])
        print("marks : ",data["marks"])
        break
else:
     print("student not found")    
    