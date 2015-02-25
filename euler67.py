from time import time

tri=open('triangle.txt').read().strip().split('\n')

start=time()
for x in range(len(tri)):
    tri[x]=tri[x].split(' ')
    for y in range(len(tri[x])):
        tri[x][y]=int(tri[x][y])

for u in range(len(tri)-2,-1,-1):
    for v in range(len(tri[u])):
        if tri[u][v]+tri[u+1][v]>tri[u][v]+tri[u+1][v+1]:
            tri[u][v]=tri[u][v]+tri[u+1][v]
        else:
            tri[u][v]=tri[u][v]+tri[u+1][v+1]

print(tri[0][0])
print(time()-start)
