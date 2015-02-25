from time import time
from math import factorial as bang

def ncr(n,r):
    return bang(n)/(bang(r)*bang(n-r))
t1=time()
s=0
for n in range(23,101):
    s+=n
    for r in range(1,int(n/2)):
        if ncr(n,r)>1e6:
            s-=r
            break
    for r in range(n,int(n/2)-1,-1):
        if ncr(n,r)>1e6:
            s-=(n-r)
            break
            
print(s)
print(time()-t1)
