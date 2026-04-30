# Q7.
#Write a program to count how many values in a dictionary are even and how many are odd.

num={
    "A":75,
    "B":20,
    "C":10,
    "D":90,
    "E":100
}
Ecount=0
Ocount=0

for key,value in num.items():
    if value%2==0:
        Ecount=Ecount+1
    else:
        Ocount=Ocount+1
print("even values : ",Ecount)
print("odd values : ",Ocount)            
