from time import time
start=time()

def prime_numbers(limit=1000000):
    yield 2
    sub_limit = int(limit**0.5) 
    flags = [0,0] + [1] * (limit - 2)
    for x in range(3, limit, 2):       
        if not flags[x]:
            continue
        yield x
        if x <= sub_limit:
            for y in range(x*x, limit, x<<1):
                flags[y] = 0
def rot(num):
    r=str(num)
    for x in range(len(r)-1):
        r=r[1:]+r[0]
        yield int(r)

a=set(prime_numbers())
count=0
for each in a:
    if set(rot(each)).issubset(a):
        count+=1
print(count)
print(time()-start)
