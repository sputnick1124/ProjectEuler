from time import time

def pent(n):
    return int(n*(3*n-1)/2)
def ispent(num):
    n=((24*num+1)**.5+1)/6
    if int(n)==n:
        return True
    return False
k,d=1,[]
t1=time()
while k<3000:
    k+=1
    j=k
    while True:
        j-=1
        if j==0:
            break
        if ispent(pent(j)+pent(k)) and ispent(pent(k)-pent(j)):
            d.append(pent(k)-pent(j))
print(d)
print(time()-t1)
