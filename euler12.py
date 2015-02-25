import time
import sys
sys.setrecursionlimit(4500)

start = time.time()
##def tri(s1,s2,lim,n):
##    s3 = 2*s2-s1+1
##    n+=1
##    if fctr(s3,0,0)<lim:
##        return tri(s2,s3,lim,n)
##    else:
##        return s3,n

def fctr(num,n,i):
    i = 0
    lim = num
    while i < lim:
        i+=1
        if num%i==0:
            n+=2
            lim = num/i
    return n
i = 0
n = 0
f=0
while f<500:
    i+=1
    n+=i
    f = fctr(n,0,0)
##h = tri(0,1,322,0)
print(n)
print(time.time()-start)
