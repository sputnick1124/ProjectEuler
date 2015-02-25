from time import time
t1=time()

words=[]
f1=open('words.txt')
f=f1.read().split(',')
f1.close()
for each in f:
    words.append(each.strip('"'))

trianglenums=set(n*(n+1)/2 for n in range(1,20))

alpha=list('0abcdefghijklmnopqrstuvwxyz'.upper())
count=0
for word in words:
    wordvalue=0
    for letter in word:
        wordvalue+=alpha.index(letter)
    if wordvalue in trianglenums:
        count+=1
print(count)
print(time()-t1)
