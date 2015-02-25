from time import time

def CF(n,m=None,d=None,a=None,flag=None,a0=None):
    if m is None:
        a0=int(n**.5)
        if a0==n**.5:
            return 0
        m,d,a,flag=0,1,a0,0
    m1=d*a-m
    d1=(n-m1*m1)/d
    a1=int((a0+m1)/d1)
    flag+=1
    if a1==2*a0:
        return flag
    return CF(n,m1,d1,a1,flag,a0)

t1=time()
print(len([x for x in range(10001) if CF(x)%2]))
print(time()-t1)
