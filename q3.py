# Q3.
# Write a program to add a new key-value pair to a dictionary. If the key already exists, update its value.

num={
    "A":10,
    "B":20,
    "C":50
}

key=input("enter key : ")
value=input("enter values : ")
num[key]=value 
print(num)