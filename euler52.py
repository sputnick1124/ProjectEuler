#It can be seen that the number, 125874, and its double, 251748, contain 
#exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
#contain the same digits.
from time import time
def isperm(n1):
    t1=set(str(n1))
    if len(t1)==len(str(n1)):
        t2=(set(str(n1*n)) for n in range(2,7))
        return all(t1.issubset(it) for it in t2)
    return False
t1=time()
n=5
c=10**n
while not isperm(c):
    c+=1
    if int(c/10**n)>1:
        n+=1
        c=10**n
print(c)
print(time()-t1)
