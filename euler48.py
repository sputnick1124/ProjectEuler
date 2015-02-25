from time import time
t1=time()
print(str(sum(x**x for x in range(1001)))[-10:])
print(time()-t1)
