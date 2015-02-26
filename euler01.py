from time import time
t1=time()
print(sum(n for n in range(3,1000) if not n%3 or not n%5))
print(time()-t1)
t2=time()
print(sum(list(set(range(3,1000,3))|set(range(5,1000,5)))))
print(time()-t2)
