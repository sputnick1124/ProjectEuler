from time import time

t1=time()
print(max(sum(int(d) for d in str(n**m)) for n in range(101) for m in range(101)))
print(time()-t1)
