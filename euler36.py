from time import time
def is_ten_pal(num):
    if str(num)==str(num)[::-1]:
        return is_bin_pal(bin(num)[2:])
    return False
def is_bin_pal(string):
    if string==string[::-1]:
        return True
    return False

t1=time()
s=sum([x for x in range(1,int(1e6),2) if is_ten_pal(x)])
print(s,time()-t1)
