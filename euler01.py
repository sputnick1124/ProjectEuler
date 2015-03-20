from time import time
from sys import argv
n = int(argv[1])
#t1=time()
#print(sum(x for x in range(3,n) if not x%3 or not x%5))
#print(time()-t1)
#t2=time()
#print(sum(list(set(range(3,n,3))|set(range(5,n,5)))))
#print(time()-t2)
sum = 0
for x in xrange(n):
	if not x%3 or not x%5:
		sum += x
print sum
