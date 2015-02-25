from time import time

def reduce(lst):
    den,num=lst[0],lst[1]
    for x in range(int(num),1,-1):
        if not den%x and not num%x:
            return reduce([den/x,num/x])
    return '%d/%d'%(num,den)

t1=time()
scf=[1,1]
for x in range(1,10):
    for y in range(1,10):
        for z in range(1,10):
            if y!=z and (y+x*10)/(x+z*10)==y/z:
                scf=[scf[0]*(y+x*10),scf[1]*(x+z*10)]
print(reduce(scf))
print(time()-t1)
