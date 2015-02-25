from time import time

def orderedlist(c):
    c=list(str(c))
    return ''.join(sorted(c))

t1=time()
n=216
pdict={}
l=5
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
        print(min(pdict[rp]))
        print(time()-t1)
        break
    n+=1
