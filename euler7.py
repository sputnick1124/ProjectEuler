import time
start = time.time()
n = 10001
primes = [2,3]
 
while len(primes)<n:
    l = len(primes)+1
    x = primes[-1]
    while len(primes)<l:
        x += 2
        for i in primes:
            if x%i==0:
                break
            else:
                next
            if i==primes[-1]:
                primes.append(x)
print(primes[-1])
print(time.time()-start)
