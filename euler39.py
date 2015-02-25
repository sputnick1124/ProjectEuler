from time import time

def pyth_trip(limit=1000):
    for n in range(1,limit):
        for m in range(n,limit):
            if m*m+n*n>limit:
                break
            for k in range(1,limit):
                if k*(m*m+n*n)>limit:
                    break
                yield k*(m*m-n*n),k*2*m*n,k*(m*m+n*n)
t1=time()
p=list(sum(x) for x in set(pyth_trip()) if sum(x)<=1000)
n=0
opt=0
for each in set(p):
    if p.count(each)>n:
        n=p.count(each)
        opt=each
print(opt)
print(time()-t1)
