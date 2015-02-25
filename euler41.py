from time import time

def primes(limit=100000000):
    sub_lim=int(limit**.5)
    flag=[0,0]+[1]*(limit-2)
    for x in range(3,limit,2):
        if not flag[x]:
            continue
        if ispan(x):
            yield x
        if x<=sub_lim:
            for y in range(x*x,limit,x<<1):
                flag[y]=0
def ispan(num):
    return set(str(num)).issubset(set(str(x) for x in range(1,len(str(num))+1))) and len(set(str(num)))==len(str(num))
t1=time()
print(max(primes(1000000)))
print(time()-t1)
