# Q2.
# Write a program to check whether a given key exists in a dictionary. If it exists, print its value; otherwise, print “Key not found”.

num={
    "A":10,
    "B":20,
    "C":50
}

k=input("enter a key you want to found : ")
if k in num:
    print("key found")
    print("value of key is : ",num[k])

else:
    print("key not found")
     

