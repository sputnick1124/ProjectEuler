from time import time

def appr(a,num=1,den=0):
    if not a:
        return 2*den+num,den
    if not den:
        den=a.pop()
        return appr(a,num,den)
    den1=den*a.pop()+num
    num=den
    return appr(a,num,den1)

t1=time()
a=[2*(x+1)//3 if not (x+1)%3 else 1 for x in range(1,100)]
e0=appr(a)
print(sum(map(int,str(e0[0]))))
print(time()-t1)
    


