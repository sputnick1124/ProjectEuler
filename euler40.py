from time import time

def champ(limit=1000000):
    f='0'
    i=0
    while len(f)<=limit:
        i+=1
        f+=str(i)
    return f
t1,a,p=time(),list(champ()),1
for n in range(7):
    p*=int(a[10**n])
print(p)
print(time()-t1)
