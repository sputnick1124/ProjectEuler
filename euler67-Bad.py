from time import time
start=time()
tri=open('triangle.txt').read().strip().split('\n')


for x in range(len(tri)):
    tri[x] = tri[x].split(' ')
    for y in range(len(tri[x])):
        tri[x][y] = int(tri[x][y])

m = 0
for v in xrange(1,2**99):
    s = 0
    b = '0'*(100-len(bin(v).split('b')[-1]))+bin(v).split('b')[-1]
    ind = 0
    for u in xrange(len(tri)):
        if int(b[u]):
            s += tri[u][ind+1]
            ind+=1
        else:
            s += tri[u][ind]
    if s>m:
        m=s
print(m)
print(time()-start)
