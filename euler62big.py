from time import time

def orderedlist(c):
    c=list(str(c))
    return ''.join(sorted(c))

t1=time()
n=216
pdict={}
ldict={n: set() for n in range(4,251)}
l=25
while True:
    p=orderedlist(n**3)
    ld=len(p)
    if p in pdict.keys():
        pdict[p].add(n)
    else:
        pdict[p]={n}
    if len(pdict[p])==l:
        rp=p
        while len(p)==ld:
            p=orderedlist(n**3)
            if p in pdict.keys():
                pdict[p].add(n)
            else:
                pdict[p]={n}
            if len(pdict[p])==l and min(pdict[p])<min(pdict[rp]):
                rp=p
            n+=1
        break
    n+=1
for k in pdict.keys():
    if len(pdict[k]) in ldict.keys():
        ldict[len(pdict[k])].add(min(pdict[k]))

for k in ldict.keys():
    print(k,min(ldict[k]))
print('%s seconds' % str(time()-t1)[:5])
