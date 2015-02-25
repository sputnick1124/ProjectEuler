from time import time
from math import log
from primes import primes, isprime

def concatp(p1,p2):
    d1=int(log(p1,10)+1)
    d2=int(log(p2,10)+1)
    if not isprime(p1*10**d2+p2):
        return False
    if not isprime(p2*10**d1+p1):
        return False
    return True
t1=time()
primelist=[p for p in primes(10000,3) if not p==5]
psets={}
winners=[]
for n1,p1 in enumerate(primelist):
    if p1==5:
        continue
    psets[p1]=set()
    for p2 in primelist[:n1]+primelist[n1+1:]:
        if concatp(p1,p2):
            psets[p1].add(p2)

for p1 in psets:
    for p2 in psets[p1]:
        set2=psets[p1]&psets[p2]
        if set2:
            for p3 in set2:
                set3=set2&psets[p3]
                if set3:
                    for p4 in set3:
                        set4=set3&psets[p4]
                        if set4:
                            p5=set4.pop()
                            set5={p1,p2,p3,p4,p5}
                            if not set5 in winners:
                                winners.append(set5)
for each in winners:
    print(each,sum(each))
print(time()-t1)
