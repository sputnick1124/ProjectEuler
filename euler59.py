from time import time
from itertools import permutations as perms

def dc(iterable,ok):
    t,s='',0
    for x in iterable:
        char=x[0]^x[1]
        if char in ok:
            t+=chr(char)
            s+=char
        else:
            return False
    return t,s
t1=time()
##ok=set(range(32,123))
ok=set([32,33,39,40,41,44,46,
    59]+list(range(48,58))+list(range(65,91))+list(range(97,123)))
cipher=eval(open('cipher1.txt').read())
##decrypt=[]
al = {x: ord(x) for x in set('abcdefghijklmnopqrstuvwxyz')}
keys=(perms(al.values(),3))
for key in keys:
    mask=key*400+(key[0],)
    text=dc(zip(cipher,mask),ok)
    if text:
        print(text[1])
        break
        decrypt.append(text)
print(time()-t1)
