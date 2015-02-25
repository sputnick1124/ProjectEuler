from time import time
start = time()

def is_abundant(num):
    sums=1
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            sums+=i+num/i
            if num/i==i:
                sums-=i
    if sums>num:
        return 1
    else:
        return 0
def is_abundant_sum(num,alist):
    for each in alist:
        if each>num:
            return 0
        if num-each in alist:
            return 1
    return 0

alist=set()
asum=0
for x in range(1,28124):
    if is_abundant(x):
        alist.add(x)
    if not any(x-n in alist for n in alist):
        asum+=x

print(asum)
print(time()-start)

