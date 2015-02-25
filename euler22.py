from time import time
start = time()
f=open('names.txt')
names=f.readlines()
f.close()

names=names[0].strip('"').split('","')
names.sort()
letters = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']

prodsum=0
for name in names:
    index=names.index(name)+1
    lettersum=0
    for letter in name:
        lettersum+=letters.index(letter)
    prodsum+=lettersum*index

print(prodsum)
print(time()-start)
