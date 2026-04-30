#Q11.
#Write a program to find the first non-repeating character in a string.

s=input("enter string : ")
for i in range(len(s)):
    count=0
    for j in range(len(s)):
        if s[i]==s[j]:
          count=count+1
    if count==1:
       print("first non repeating : ",s[i])
       break
    else:
       print("no first repeating")      

