from time import time
t1=time()
prods=set()
for x in range(1,98):
    if len(set(str(x)))<len(str(x)) or '0' in str(x):
        continue
    for y in range(123,9877):
        if len(set(str(y)))==len(str(y)) and '0' not in str(y):
            if len(str(x)+str(y)+str(x*y))>9:
                break
            if not len(set(str(x)).intersection(set(str(y)))):
                if not len(set(str(x)).symmetric_difference(set(str(y))).intersection(set(str(x*y)))):
                    if len(set(str(x*y)))==len(str(x*y)):
                        if len(set(str(x)+str(y)+str(x*y)))==9 and '0' not in str(x*y): 
                            prods.add(x*y)
print(sum(prods))
print(time()-t1)
