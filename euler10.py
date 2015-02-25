import time
start = time.time()

n=2e6
p=1
s = 2
while p<n:
    prime=1
    p+=2
    lim=int(p**(1/2))+1

    for x in range(2,lim):
        if p%x==0:
            prime=0
            break
    if prime==1:
        s+=p

print(s)
print(time.time()-start)
