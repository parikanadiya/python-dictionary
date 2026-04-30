#Q12.
#Given a list of words, create a dictionary where the key is the length of the word and the value is a list of words of that length.

li=["pari","hi","hello","no","gone"]
dict={}
for word in li:
    length=len(word)

    if length in dict:
      dict[length].append(word)
    else:
      dict[length]=[word]
print(dict)        


#{4: ['pari', 'gone'], 2: ['hi', 'no'], 5: ['hello']}