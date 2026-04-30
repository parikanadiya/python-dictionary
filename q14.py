# Q14.
# Write a program to merge two dictionaries. If a key is common, add their values; otherwise, keep the values as they are.

num={
    "A":75,
    "B":20,
    "C":10,
    "D":90,
    "E":100
}
num1={
    "A":75,
    "B":20,
    "C":10,
    "D":90,
    "E":100
}
new={}

for key,value in num.items():
    new[key]=value

for key,value in num1.items():
    if key in new:
       new[key]+=value
    else:
        new[key]=value
print(new)           
        
