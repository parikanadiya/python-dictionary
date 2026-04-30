# This is the structure for nested Dictionaries. Follow this and ask details from the user. 

# students = {
# 1: {"name": "Rahul", "marks": 80},
# 2: {"name": "Priya", "marks": 65},
# 3: {"name": "Amit", "marks": 90}
# }

stu={}
n=int(input("enter num of students : "))

for i in range(1,n+1):
    print(f"\n enter details for student{i}")
    name=input("enter name : ")
    marks=input("enter marks : ")

    stu[i]={
        "name":name,
        "marks":marks
    }
  
print("student data")
for key,value in stu.items():
    print(key,":",value)  


#     student data
# 1 : {'name': 'pari', 'marks': '89'}
# 2 : {'name': 'hetvi', 'marks': '78'}
# 3 : {'name': 'kiran', 'marks': '90'}

print("student data")

print("students={")
for key,value in stu.items():
    print(key,":",value)
print("}")    

