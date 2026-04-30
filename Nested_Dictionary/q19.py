# Q19.
# Write a program to delete a student record using student ID.

students={
    1:{"name":"pari","marks":67},
    2: {"name": "Priya", "marks": 65},
    3: {"name": "Amit", "marks": 90}

}

s_id=int(input("enter id you want to delete : "))

if s_id not in students:
    print("Id invalid not present")

else:
  del students[s_id]
  print("student id deleted successfully")    

print("updated")
print(students)


