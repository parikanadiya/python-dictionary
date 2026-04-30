# Q13.
# Write a program to swap keys and values in a dictionary. 
num={
    "A":70,
    "B":20,
    "C":10,
    "D":90,
    "E":100
}
swap={}
print("before swapped : ",num)
print("after swapping : ")
for key,value in num.items():
    swap[value]=key
print(swap)    

