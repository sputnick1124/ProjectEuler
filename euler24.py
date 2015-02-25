from math import factorial as fact
from time import time
start = time()
n=0
steps=[]
while n<1e6:
    for x in range(9,0,-1):
        for y in range(x+1):
            if n+fact(x)*y==1e6:
                n+=fact(x)*y
                steps.append(y-1)
                break
            if n+fact(x)*(y+1)>1e6:
                n+=fact(x)*y
                steps.append(y)
                break
perm1 = list(range(10))
perm1e6 = ''
for each in steps:
    perm1e6+=str(perm1[each])
    del perm1[each]
for each in perm1:
    perm1e6+=str(each)
print(perm1e6)
print(time()-start)
