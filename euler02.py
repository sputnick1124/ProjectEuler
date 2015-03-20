from time import time
from collections import deque
from sys import argv

n = int(argv[1])
fibs = deque([1,1])
count = 0
t1=time()
while fibs[-1] < n:
    fibs.append(fibs.popleft() + fibs[0])
    count += fibs[-1] if not fibs[-1]%2 else 0

print(count)
print(time()-t1)
