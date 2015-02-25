from time import time

def primes(limit=1000000):
    yield 2
    sublim=int(limit**.5)
    flag=[0,0]+[1]*(limit-2)
    for x in range(3,limit,2):
        if not flag[x]:
            continue
        yield x
        if x<=sublim:
            for y in range(x*x,limit,x<<1):
                flag[y]=0
def comps(limit=1000000):
    yield 9
    sublim=int(limit**.5)
    flag=[1]*10+[0]*(limit-10)
    for x in range(3,limit,2):
        if flag[x]:
            if x>9:
                yield x
        if x<=sublim:
            for y in range(x*x,limit,x<<1):
                flag[y]=1
t1=time()
for comp in comps():
    if not any(int(((comp-x)/2)**.5)==((comp-x)/2)**.5 for x in primes(comp)):
        print(comp)
        print(time()-t1)
        break
