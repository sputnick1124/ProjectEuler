from time import time
from primes import isprime
##def isprime(p):
##    if not p%2:
##        return False
##    for n in range(3,int(p**.5),2):
##        if not p%n:
##            return False
##    return True

t1=time()
p=0
diags=1
for square in range(3,99999,2):
    diags+=4
    for corner in range(1,4):
        if isprime((square-2)**2+corner*(square-1)):
            p+=1
    if p/diags<=.1:
        print(square)
        break
print(time()-t1)
