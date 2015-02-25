from time import time

def primes():
    yield 2
    sublim=int(1000000**.5)
    flag=[0,0]+[1]*999998
    for x in range(3,1000000,2):
        if not flag[x]:
            continue
        yield x
        if x<=sublim:
            for y in range(x*x,1000000,x<<1):
                flag[y]=0
def primeFactor(num,f):
    if num in primes():
        f.append(num)
        return f
    for x in primes():
        if not num%x:
            f.append(x)
            return primeFactor(num/x,f)
        if num==1:
            return f

t1=time()
found=False
n=130000
while found is  False:
    n+=1
    if len(set(primeFactor(n,[])))==4:
        n+=1
        if len(set(primeFactor(n,[])))==4:
            n+=1
            if len(set(primeFactor(n,[])))==4:
                n+=1
                if len(set(primeFactor(n,[])))==4:
                    print(n-3)
                    print(time()-t1)
                    found=True

