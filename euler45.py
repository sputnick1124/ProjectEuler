from time import time

def ispent(num):
    n=((24*num+1)**.5+1)/6
    return int(n)==n
def ishex(num):
    n=((8*num+1)**.5+1)/4
    return int(n)==n
def isall(num):
    return ispent(num) and ishex(num)
t1=time()
tph=40755
t=285
while tph==40755:
    t+=1
    tri=(t*t+t)/2
    if isall(tri):
        tph=tri
print(tri)
print(time()-t1)
