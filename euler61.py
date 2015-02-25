from time import time

def trinum(n): return n*(n+1)//2
def sqnum(n): return n*n
def pentnum(n): return n*(3*n-1)//2
def hexnum(n): return n*(2*n-1)
def heptnum(n): return n*(5*n-3)//2
def octnum(n): return n*(3*n-2)

def triin(p): return ((8*p+1)**.5-1)/2
def sqin(p): return p**.5
def pentin(p): return ((24*p+1)**.5+1)/6
def hexin(p): return ((8*p+1)**.5+1)/4
def heptin(p): return ((40*p+9)**.5+3)/10
def octin(p): return ((12*p+4)**.5+2)/6

def nexttri(p): return trinum(int(triin(p)+1))
def nextsq(p): return sqnum(int(sqin(p)+1))
def nextpent(p): return pentnum(int(pentin(p)+1))
def nexthex(p): return hexnum(int(hexin(p)+1))
def nexthept(p): return heptnum(int(heptin(p)+1))
def nextoct(p): return octnum(int(octin(p)+1))

def searchtree(seed1,flags={1,2,3,4,5,6}):
    seed=(seed1-seed1//100*100)*100
    if 1 in flags:
        tri=nexttri(seed)
        while tri<seed+100:
            while str(tri)[-2]=='0':
                tri=nexttri(tri)
            triflag=flags-{1}
            if tri<seed+100:
                yield tri,triflag,seed1
            tri=nexttri(tri)
    if 2 in flags:
        sq=nextsq(seed)
        while sq<seed+100:
            while str(sq)[-2]=='0':
                sq=nextsq(sq)
            sqflag=flags-{2}
            if sq<seed+100:
                yield sq,sqflag,seed1
            sq=nextsq(sq)
    if 3 in flags:
        pent=nextpent(seed)
        while pent<seed+100:
            while str(pent)[-2]=='0':
                pent=nextpent(pent)
            pentflag=flags-{3}
            if pent<seed+100:
                yield pent,pentflag,seed1
            pent=nextpent(pent)
    if 4 in flags:
        hex1=nexthex(seed)
        while hex1<seed+100:
            while str(hex1)[-2]=='0':
                hex1=nexthex(hex1)
            hexflag=flags-{4}
            if hex1<seed+100:
                yield hex1,hexflag,seed1
            hex1=nexthex(hex1)
    if 5 in flags:
        hept=nexthept(seed)
        while hept<seed+100:
            while str(hept)[-2]=='0':
                hept=nexthept(hept)
            heptflag=flags-{5}
            if hept<seed+100:
                yield hept,heptflag,seed1
            hept=nexthept(hept)
    if 6 in flags:
        oct1=nextoct(seed)
        while oct1<seed+100:
            while str(oct1)[-2]=='0':
                oct1=nextoct(oct1)
            octflag=flags-{6}
            if oct1<seed+100:
                yield oct1,octflag,seed1
            oct1=nextoct(oct1)  

t1=time()
seeds=[[]]
tri=1010
end=False
while nexttri(tri)<10000:
    tri=nexttri(tri)
    while str(tri)[-2]=='0':
        tri=nexttri(tri)
    seeds[0].append((tri,{2,3,4,5,6}))
    
while not end:
    seeds.append([])
    for root in seeds[-2]:
        for branch in searchtree(*root[:2]):
            if not len(branch[1]):
                if str(branch[0])[-2:]==str(root[-1])[:2]:
                    seeds[-1].append((branch[2],)+root[2:]+(branch[0],))
                    end=True
            elif branch:
                seeds[-1].append(branch+root[2:])
                
print(seeds[-1][0],sum(seeds[-1][0]))
print(time()-t1)
