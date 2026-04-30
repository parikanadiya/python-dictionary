# Q9.
# Write a program to count the frequency of each character in a given string using a dictionary.
s=input("enter string : ")
freq={}

for ch in s:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1    
print(freq)
for key,value in freq.items():
    print(key,":",value)        
