from time import time
from sys import setrecursionlimit

def frac_exp(n,num=5,den=2):
    if n==1:
        return len(str(den+num))>len(str(num))
    return frac_exp(n-1,2*num+den,num)

setrecursionlimit(1500)
t1=time()
s=0
for n in range(7,1001):
    if frac_exp(n):
        s+=1
print(s)
print(time()-t1)
