from time import time

def isPrime(num):
    if num<=0:
        return False
    for x in range(3,int(num**.5),2):
        if not num%x:
            return False
    return True
def quadPrime(a,b):
    count=0
    n=0
    while True:
        if not isPrime(n*n+a*n+b):
            return n-1
            break
        n+=1
def primeNumber(limit=1000):
    yield 2
    sub_lim=int(limit**.5)
    flag=[0,0]+[1]*(limit-2)
    for x in range(3,limit,2):
        if not flag[x]:
            continue
        yield x
        if x<=sub_lim:
            for y in range(x*x,limit,x<<1):
                flag[y]=0
t1=time()
maxNum=[0,0,0]
primes=set(primeNumber())
for a in range(-999,1000):
    for b in primes:
        qP=quadPrime(a,b)
        if qP>maxNum[0]:
            maxNum=[qP,a,b]
print(maxNum[1]*maxNum[2])
print(time()-t1)
                
        
