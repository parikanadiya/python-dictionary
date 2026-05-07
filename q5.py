# Q5.
# Given a dictionary with numeric values, write a program to find the key having the maximum value.

num={
    "A":10,
    "B":20,
    "C":50
}

maximun=max(num.values())

for key,value in num.items():
    if value==maximun:
      print("maximum value : ",value)
      print("maximum key : ",key