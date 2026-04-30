# Q10.
# Write a program to count the frequency of each word in a given sentence.

sen=input("enter a sentence : ") #hi hello hi pari pari hi 
freq={}
word=""

for ch in sen:
    if ch!=" ":  #h->hi->_
        word=word+ch #hi
    else:
      if word!="": #hi no space after
            if word in freq:
              freq[word]=freq[word]+1 #hi=1
           
            else:
              freq[word]=1  
            word="" #again word is empty

if word!="":
        if word in freq:
              freq[word]=freq[word]+1
        else:
            freq[word]=1 

for k,v in freq.items():
    print(k,":",v)            