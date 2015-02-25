# this code is broken. It does not find multiple instances of a value in the
# sum string. Implement a loop or recursion to fix.
from time import time
start = time()

def fctr(num,n=0,i=0):
    lim = num
    while i < lim-1:
        i+=1
        if num%i==0:
            n+=i
            lim = num
    if n>10000 or n==num:
        n=0
    return n

s = []
a = []
for x in range(10001):
    s.append(fctr(x))
for each in s:
    if s.index(each)==s[each]:
        if each not in a:
            a.append(each)
print(sum(a))
print(time()-start)
