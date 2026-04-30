# Q16.
# Write a program to display the names of students who have scored more than 75 marks

# students = {
#  1: {"name": "Rahul", "marks": 80},
#  2: {"name": "Priya", "marks": 65},
#  3: {"name": "Amit", "marks": 90}
#  }

# for key,value in students.items():
#     if value["marks"]>75:
#         print(value["name"])


#using user input

stu={}
num=int(input("enter number of students : "))

for i in range(1,num+1):
    print(f"enter details of student {i}")

    name=input("enter name : ")
    marks=int(input("enter marks : "))

    stu[i]={
        "name":name,
        "marks":marks

    }

for key,value in stu.items():
    print(key,":",value)   

if value["marks"]>75:
   print(value["name"])


