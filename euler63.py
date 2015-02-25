from time import time

t1=time()
n,c=1,0
for x in range(1,10):
    n=1
    while x**n<10**(n-1):
        n+=1
    while len(str(x**n))==n:
        c+=1
        n+=1
print(c)
print(time()-t1)
