##A palindromic number reads the same both ways.
##The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
##Find the largest palindrome made from the product of two 3-digit numbers.
from time import time
t1=time()
palin = []
for x in range(110,1000,11):
    for y in range(x,1000):
        parse = []
        check = x*y
        while check>0:
            parse.append(check-10*(int(check/10)))
            check = int(check/10)
        parse = parse[::-1]
        if len(parse)%2==0:
            a = parse[:int(len(parse)/2)]
            b = parse[int(len(parse)/2):]
        else:
            a = parse[:int(len(parse)/2)]
            b = parse[int(len(parse)/2)+1:]
        if a==b[::-1]:
            palin.append(x*y)
print(max(palin))
print(time()-t1)
