# Q15.
# Write a program to create a new dictionary by multiplying all values in the given dictionary by 2.

num={
    "A":7,
    "B":20,
    "C":10,
    "D":9,
    "E":10
}

new={}
for key,value in num.items():
    new[key]=value*2
print(new)    
