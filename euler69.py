from __future__ import division
from time import time
from primes import factor

def totient(n):
    fx=set(factor(n))
    for x in fx:
        n*=(1-1/x)
    return n

t1=time()
limit=1000000
#pq,phi={},{}
#for x in range(2,limit):
#    if not x%10000:
#        print x
#    flag={1}
#    fx=set(factor(x))
#    for y in fx:
#        for m in range(y,x,y):
#            flag.add(m)
#    phi[x]=x-len(flag)
#    pq[x]=(x/phi[x],x)
#print(max(pq.values()))
m=0
for n in range(2,limit):
    t=totient(n)
    if n/t>m:
        m=t
        d=n
print(m,d)
print(time()-t1)

