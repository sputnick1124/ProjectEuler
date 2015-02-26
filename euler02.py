from time import time

fibs = [1,1]
count,sums = 0,0
t1=time()
while fibs[count+1] + fibs[count] < 4e6:
    fibs.append(fibs[count] + fibs[count+1])
    count = count + 1


for i in fibs:
    if i%2 == 0:
        sums+=i

print(sums)
print(time()-t1)