from time import time

def primes(limit=1000000):
    sublim=int(limit**.5)
    flag=[0,0]+[1]*(limit-2)
    for x in range(3,limit,2):
        if not flag[x]:
            continue
        if not len(set(str(x)))==len(str(x)):
            psl=list(str(x))
            for digit in list(set(str(x))):
                psl.remove(digit)
            for n in set(psl):
                if n in {'0','1','2'}:
                    yield x,n
        if x<=sublim:
            for y in range(x*x,limit,x<<1):
                flag[y]=0
def primes1(limit=1000000):
    sublim=int(limit**.5)
    flag=[0,0]+[1]*(limit-2)
    for x in range(3,limit,2):
        if not flag[x]:
            continue
        yield x
        if x<=sublim:
            for y in range(x*x,limit,x<<1):
                flag[y]=0
def rep(prime):
    mask=''
    for digit in str(prime[0]):
        if digit == prime[1]:
            mask+='1'
        else:
            mask+='0'
    im=int(mask)
    return [im*n for n in range(1,10-int(prime[1]))]

t1=time()
allprimes=set(primes1())
drp=primes()
c=[]
for prime in drp:
    r=rep(prime)
    if len([prime[0]+rp for rp in r if prime[0]+rp in allprimes])>6:
        print(prime[0])
        break
print(time()-t1)
