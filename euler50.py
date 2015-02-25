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
t1=time()
longest=[0,0,0]
limit=10000000
primelist=list(primes(limit))
for i in range(len(primelist)):
    s=sum(primelist[:i])
    if s>limit:
        break
    if s in primelist and s<limit:
        start=i
for x in range(len(primelist)):
    if sum(primelist[x:x+start])>limit:
        break
    for y in range(start,len(primelist)):
        sn=sum(primelist[x:y])
        if sn>limit:
            break
        if sn in primelist and y-x>longest[-1]-longest[-2]:
            longest=[sn,x,y]

print(longest)
print(time()-t1)
