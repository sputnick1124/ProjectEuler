import time
start = time.time()

def collatzer(num,n):
    if num==1:
        return n
    elif num%2==0:
        num/=2
        return collatzer(num,n+1)
    else:
        num = (3*num+1)/2
        return collatzer(num,n+2)

l = 0

for i in range(1,1000001):
    if collatzer(i,0)>l:
        l = collatzer(i,0)
        n = i

print(n)
print(time.time()-start)
