from time import time

def ispan(s):
        if len(s)==len(set(s)):
            return True
        return False
            
t1=time()
s=0
digits=set('1234567890')
for a in range(10,1000,2):
    if len(str(a))<3:
        a='0'+str(a)
    else:
        a=str(a)
    for b in range(12,1000,3):
        if len(str(b))<3:
            b='0'+str(b)
        else:
            b=str(b)
        if a[-2:]==b[:2]:
            ab=a+b[-1]
        else:
            continue
        for c in range(10,1000,5):
            if len(str(c))<3:
                c='0'+str(c)
            else:
                c=str(c)
            if b[-2:]==c[:2]:
                abc=ab+c[-1]
            else:
                continue
            for d in range(14,1000,7):
                if len(str(d))<3:
                    d='0'+str(d)
                else:
                    d=str(d)
                if c[-2:]==d[:2]:
                    abcd=abc+d[-1]
                else:
                    continue
                for e in range(11,1000,11):
                    if len(str(e))<3:
                        e='0'+str(e)
                    else:
                        e=str(e)
                    if d[-2:]==e[:2]:
                        abcde=abcd+e[-1]
                    else:
                        continue
                    for f in range(13,1000,13):
                        if len(str(f))<3:
                            f='0'+str(f)
                        else:
                            f=str(f)
                        if e[-2:]==f[:2]:
                            abcdef=abcde+f[-1]
                        else:
                            continue
                        for g in range(17,1000,17):
                            if len(str(g))<3:
                                g='0'+str(g)
                            else:
                                g=str(g)
                            if f[-2:]==g[:2]:
                                abcdefg=abcdef+g[-1]
                                if ispan(abcdefg):
                                    missing=digits-set(abcdefg)
                                    s+=int(str(list(missing)[0])+abcdefg)
                            else:
                                continue
print(s)
print(time()-t1)


