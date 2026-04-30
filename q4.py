# Q4.
# Write a program to remove a key from a dictionary. If the key is not present, display an appropriate message.


num={
    "A":10,
    "B":20,
    "C":50
}
remove=input("enter key you want to remove : ")
if remove in num:
    num.pop(remove)
    print("key removed ")
    
else:
    print("key not found")   

print(num)     