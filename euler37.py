from time import time

def primes(limit=1000000):
    yield 2
    sub_lim=int(limit**.5)
    flag=[0,0]+[1]*(limit-2)
    for x in range(3,limit,2):
        if not flag[x]:
            continue
        if set(str(x)).issubset({'1','2','3','5','7','9'}):
            yield x
        if x<=sub_lim:
            for y in range(x*x,limit,x<<1):
                flag[y]=0
def trunc(prime):
    truncs=set()
    temp1=str(prime)
    temp2=str(prime)
    for x in range((len(temp1)-1)):
        truncs.add(int(temp1[1:]))
        truncs.add(int(temp2[:-1]))            
        temp1=temp1[1:]
        temp2=temp2[:-1]
    return truncs
t1=time()
p=set(primes())
sums=0
for each in p:
    if each>10:
        if trunc(each).issubset(p):
            sums+=each
print(sums)
print(time()-t1)
