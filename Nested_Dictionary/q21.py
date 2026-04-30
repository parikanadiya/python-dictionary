# Q21.
# Write a program to assign grades to each student based on marks:
# Above 75 → Grade A
# Between 50 and 75 → Grade B
# Below 50 → Grade C

students={
    1:{"name":"pari","marks":67},
    2: {"name": "Priya", "marks": 65},
    3: {"name": "Amit", "marks": 90}

}

for data in students.values():
    marks=data["marks"]

    if marks>75:
        data["grade"]="A"
    elif marks>=50:
        data["grade"]="B"
    else:
        data["grade"]="C"

for s,data in students.items():
    print(s,":",data)                
