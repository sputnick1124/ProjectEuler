from time import time
import primes

def chakra(N,a=None,b=None,k=None):
    if k==1:
        return a
    if b is None:
        b=1
        a1=int((N*b)**.5)
        a2=a1+1
        a=(a1 if abs(a1*a1-N)<abs(a2*a2-N) else a2)
        k=a*a-N

    m1=0
    t=N-1
    while True:
        m1+=1
        if not (a+b*m1)%k:
            if abs(m1*m1-N)<t:
                t=abs(m1*m1-N)
                m=m1
            elif t!=N-1 and abs(m1*m1-N)>t:
                break
    a,b,k=(a*m+N*b)//abs(k),(a+b*m)//abs(k),(m*m-N)//k
    return chakra(N,a,b,k)

t1=time()
x,n=0,0
for N in primes.primes(1000,7):
    if int(N**.5)==N**.5:
        continue
    x0=chakra(N)
    if x0>x:
        x=x0
        n=N
print(x,n)
print(time()-t1)
