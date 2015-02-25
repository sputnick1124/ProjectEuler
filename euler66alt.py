from time import time
import primes

def CF(n,l=None,m=None,d=None,a=None,flag=None,a0=None):
    if m is None:
        a0=int(n**.5)
        if a0==n**.5:
            return 0
        m,d,a,flag=0,1,a0,[]
    m1=d*a-m
    d1=(n-m1*m1)/d
    a1=int((a0+m1)/d1)
    flag.append(a1)
    if l:
        if len(flag)==l:
            flag.insert(0,a0)
            return flag
        if a1==2*a0:
            while len(flag)<l:
                flag*=2
            flag=flag[:l]
            flag.insert(0,a0)
            return flag
    if a1==2*a0:
        flag.insert(0,a0)
        return flag
    return CF(n,l,m1,d1,a1,flag,a0)

def appr(a,num=1,den=0):
    if not a:
        return den,num
    if not den:
        den=a.pop()
        return appr(a,num,den)
    den1=den*a.pop()+num
    num=den
    return appr(a,num,den1)

def pell(N,a,b):
    return a*a-N*b*b==1

def sol(N):
    if int(N**.5)==N**.5:
        return 0
    l=2
    while True:
        a=appr(CF(N,l))
        if pell(N,*a):
            return a[0]
        l+=1
t1=time()
x0=0
for N in primes.primes(1000):
    x=sol(N)
    if x>x0:
        x0=x
        n=N

print(x0,n)
print(time()-t1)
