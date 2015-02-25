from time import time

def concat(l):
    c=''
    for num in l:
        c+=str(num)
    return c

t1=time()
maxcat=0
for x in range(8,0,-1):
    for y in range(8,0,-1):
        for z in range(8,0,-1):
            if not y==x:
                if not z==y and not z==x:
                    a=0
                    l=[]
                    while len(concat(l))<9:
                        a+=1
                        l.append((9000+x*100+y*10+z)*a)
                        if len(concat(l))==9:
                            if not any(x for x in concat(l) if concat(l).count(x)>1 or int(x)==0):
                                if int(concat(l))>maxcat:
                                    maxcat=int(concat(l))
print(maxcat)
print(time()-t1)
