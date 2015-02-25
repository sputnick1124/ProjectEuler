from time import time
from primes import factor

def totient(n):
    fx=set(factor(n))
    for x in fx:
        n*=(1-1.0/x)
    return int(n)

def isperm(m,n):
    m=list(str(m))
    m.sort()
    n=list(str(n))
    n.sort()
    return m==n

t1=time()
pq={}
for n in xrange(8075847,10000000):
    t=totient(n)
    if isperm(n,t):
        pq[n]=(n/float(t),n)
print min(pq.values())
print time()-t1