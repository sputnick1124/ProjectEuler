from time import time

start=time()
p=set()
for x in range(2,101):
    for y in range(2,101):
        if not x**y in p:
            p.add(x**y)
print(len(p))
print(time()-start)
