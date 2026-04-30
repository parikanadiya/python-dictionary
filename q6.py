# Q6.
# Write a program to create a new dictionary containing only those items whose values are greater than 50.
num={
    "A":70,
    "B":20,
    "C":10,
    "D":90,
    "E":100
}

new={}

for key,value in num.items():
    if value>50:
        new[key]=value
   
print(new)        




