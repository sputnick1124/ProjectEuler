from time import time

def f(num):
    if num==1:
        return f1(num)
    if num==3:
        return f3(num)
    if not num%2:
        return f2n(num)
    if not (num-1)%4:
        return f4n1(num)
    if not (num-3)%4:
        return f4n3(num)

def f1(num):
    return 1

def f3(num):
    return 3

def f2n(num):
    return f(num/2)

def f4n1(num):
    return 2*f(2*((num-1)/4)+1)-f((num-1)/4)

def f4n3(num):
    return 3*f(2*((num-3)/4)+1)-2*f((num-3)/4)

def S(num):
    s=0
    for x in range(1,num+1):
        s+=f(x)
    return s

def newS(num):
    s=0
    for x in range(len(bin(num)[2:])-1):
        s+=1+sum(range(1,2**x,2))
        s+=sum(range(1,num+1,2))
    return s

##start = time()
##print(str(S(3**37))[-9:-1])
##print(time()-start)
