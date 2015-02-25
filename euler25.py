from time import time
from math import log10
start = time()

def fibs(c):
    return [c[-1],sum(c)]

c,n=[1,1],2
while log10(c[-1])+1<1e3:
    c = fibs(c)
    n+=1
print(n)
print(time()-start)
