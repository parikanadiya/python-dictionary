# Q20.
# Write a program to find the student who has scored the highest marks.

students={
    1:{"name":"pari","marks":67},
    2: {"name": "Priya", "marks": 65},
    3: {"name": "Amit", "marks": 90}

}
max_m=-1
topper=""

for s in students.values():
    if s["marks"]>max_m:
        max_m=s["marks"]
        topper=s["name"]
print("topper : ",topper)
print("marks : ",max_m)        