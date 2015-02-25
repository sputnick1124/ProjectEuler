from time import time

def fourdigprimes():
    sublim=int(10000**.5)
    flag=[0,0]+[1]*9998
    for x in range(3,10000,2):
        if not flag[x]:
            continue
        if len(str(x))==4:
            yield x
        if x<=sublim:
            for y in range(x*x,10000,x<<1):
                flag[y]=0
t1=time()
primeperms=list(fourdigprimes())

for perm in primeperms:
    ind=primeperms.index(perm)
    setstrperm=set(str(perm))
    for seq in primeperms[ind:ind+int((len(primeperms)-ind)/2)]:
        if set(str(seq))==setstrperm:
            if 2*seq-perm in primeperms[ind+1:] and set(str(2*seq-perm))==setstrperm:
                print(str(perm)+str(seq)+str(2*seq-perm))
                print(time()-t1)
