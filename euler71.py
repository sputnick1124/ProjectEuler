from time import time
    
t1=time()
limit=1000000
f0=3/7.0
n,d=3.0,7.0
f=0
while d<limit:
    if n/d>=f0:
        d+=1
    else:
        n+=1
    if n/d>f:
        f=n/d
print(n)
print(time()-t1)   