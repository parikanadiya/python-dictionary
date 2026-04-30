# Q23.
# Develop a menu-driven program to manage student records using a dictionary. The program should include the following operations:
# Add student
# View all students
# Update student details
# Delete student
# Search and only display particular student (single search, multiple search, range based search for eg students having id between 10 to 20) 
# Display student with highest marks
# Display students scoring above a given value

student={}


def add_student():
    s_id=int(input("enter student id : "))

    if s_id in student:
        print("Id not exist")
    name=input("enter name of student : ")
    marks=int(input("enter marks of student : "))

    student[s_id]={
            "name":name,
            "marks":marks
        }

    print("student data added successfully")    

def view_student():

    if not student:
        print("no record found !")
        return
    for key,value in student.items():
        print(key,":",value)

def update_student():
    s_id=int(input("enter student ID you want to update : "))     

    if s_id not in student:
        print("key not found")  
        return
    print("enter what do you want to update")
    print("1.update name")
    print("2.update marks")
    print("3.update both")

    choice=int(input("enter your choice : "))

    if choice==1:
        n_name=input("enter name : ")
        student[s_id]["name"]=n_name
    elif choice==2:
        n_marks=input("enter marks : ")
        student[s_id]["marks"]=n_marks
    elif choice==3:
        n_name=input("enter name : ")
        n_marks=input("enter marks : ")
        student[s_id]["name"]=n_name
        student[s_id]["marks"]=n_marks
    else:
        print("Invalid choice") 

def delete_student():
     s_id=int(input("enter student ID you want to delete : ")) 

     if s_id not in student:
        print("student not found")  
        return
     else:
       del student[s_id]
       print("student id deleted successfully") 

def  search_student():
    print("1.single search(by name)")  
    print("2.multiple search(same name)")    
    print("3.range search(ID range)")   

    choice=int(input("enter your choice : "))

    if choice==1:
        name=input("enter name you want search first match : ").lower()
        for sid,data in student.items():
            if data["name"].lower()==name:
             print(sid,":",data)
             break
            else:
                print("student not found")

    elif choice==2: 
         name=input("enter name you want search multiple : ").lower()
         found=False
         for sid,data in student.items():
            if data["name"].lower()==name:
                print(sid,data)
                found=True

         if not found:
           print("no matching found")  

    elif choice==3:
        start=int(input("enter start ID : "))
        end=int(input("enter end ID : "))     

        for key in student.keys():
            if key>=start and key <=end:
                print(key,student[key])

def high_student():
    if not student:
        print("no data found")
        return
    max_m=-1
    topper=""

    for s in student.values():
      if s["marks"]>max_m:
         max_m=s["marks"]
         topper=s["name"]
    print("topper : ",topper)
    print("marks : ",max_m)        

def scoring_student():
    score=int(input("enter value you want to compare"))   

    for sid,data in student.items():
        if data["marks"]>=score:
            print(sid,data)                        

   
while True:
    print("----------Menu--------------")
    print("1.Add students")
    print("2.View all students")
    print("3.Update student details")
    print("4.Delete student")
    print("5.Search")
    print("6.Display student with highest marks")
    print("7.Display students scoring above a given value")
    print("8.exit")

    choice=int(input("enter your choice : "))

    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        update_student()
    elif choice==4:
        delete_student() 
    elif choice==5:
        search_student() 
    elif choice==6:
        high_student()
    elif choice==7:
        scoring_student()   
    elif choice==8:
         break
    else:
        print("please enter valid choice")  







             






