# Q8.
# Write a program to calculate the sum of all values present in a dictionary.
num={
    "A":70,
    "B":20,
    "C":10,
    "D":90,
    "E":100
}
sum=0
for key,value in num.items():
    sum=sum+value
print("total sum : ",sum)    

