from time import time
##import sys
##sys.setrecursionlimit(1500) #for large n
def fact(x,y=None):
    if y == None:
        y = x
    if y-1>0:
        x*=(y-1)
        return fact(x,y-1)
    else:
        return x
def fsum(num):
    s = 0
    for x in range(len(str(num))):
        s+=int(str(num)[x])
    return s

start = time()
print(fsum(fact(100)))
print(time()-start)
    
