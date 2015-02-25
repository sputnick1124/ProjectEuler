##In England the currency is made up of pound, £, and pence, p, and there are
##eight coins in general circulation:
##
##1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
##It is possible to make £2 in the following way:
##
##1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
##How many different ways can £2 be made using any number of coins?
from time import time
t1=time()
n=1
for p100 in range(0,300,100):
    for p50 in range(0,250,50):
        for p20 in range(0,220,20):
            for p10 in range(0,210,10):
                for p5 in range(0,205,5):
                    for p2 in range(0,202,2):
                        if sum([p2,p5,p10,p20,p50,p100])<=200:
                            n+=1
print(n,time()-t1)
