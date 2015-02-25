from time import time

t1=time()
def digfif(num):
    s=0
    for each in str(num):
        s+=eval(each)**5
    if s==num:
        return True
    return False
print(sum(x for x in range(2,6*9**5) if digfif(x)))
print(time()-t1)
