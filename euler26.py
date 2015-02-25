from time import time
from math import log10
import sys
sys.setrecursionlimit(1000)

def recip(d,c=1,rems=[]):
    c=c*10%d
    if not c:
        return 0
    if c in rems:
        return len(rems)
    rems.append(c)
    return recip(d,c,rems)
    
start = time()
n=(0,0)
for x in range(2,1001):
    if recip(x,1,[])>n[0]:
        n=(recip(x,1,[]),x)
print(n[-1])
print(time()-start)
