from time import time

def islychrel(num,i=0):
    i+=1
    s=int(str(num)[::-1])+num
    l=str(s)
    if l==l[::-1]:
        return False
    if i==50:
        return True
    return islychrel(s,i)

t1=time()
print(sum(1 for n in range(10000) if islychrel(n)))
print(time()-t1)
