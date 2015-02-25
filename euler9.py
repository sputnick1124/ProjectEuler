##A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##
##a2 + b2 = c2
##For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
##
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.
import time
def isintpy(a,b):
    c = (a**2 + b**2)**.5
    if c==int(c):
        return 1
    else:
        return 0
def multcheck(b,a):
    if b[0]/a[0]==b[1]/a[1]:
        return 1
    else:
        return 0
def thousum(pair):
    if 1000%(pair[0]+pair[1]+(pair[0]**2+pair[1]**2)**.5)==0:
        if pair[0]+pair[1]+(pair[0]**2+pair[1]**2)**.5==1000:
            return pair[0]*pair[1]*(pair[0]**2+pair[1]**2)**.5
        else:
            return pair
    else:
        return 0


start = time.time()
trips = []
ans = 0

for x in range(1,20):
    for y in range(x+1,20):
        if isintpy(x,y):
            trips.append([x,y])
            for each in trips[:-2]:
                if len(trips)>1 and multcheck(trips[-1],each)==1:
                    del trips[-1]

for each in trips:
    if thousum(each):
        if len(thousum(each))>0:
            kern = thousum(each)
            c = 1
            while isinstance(ans,list) or ans == 0:
                c+=1
                ans = thousum([c*kern[0],c*kern[1]])

print(ans)
t = time.time()-start
print('Time elapsed: %s' % t)
 
