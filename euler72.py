from time import time
from primes import factor

def func(num):
    fracs = num - 1
    for x in range(2,num):
        for y in range(x+1,num+1):
            if y%x:
                if not set(factor(y))&set(factor(x)):
                    fracs += 1
    return fracs
    
    
t1 = time()
print func(50)
print time() - t1
