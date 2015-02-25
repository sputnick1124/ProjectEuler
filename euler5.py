import time
start = time.time()
prod = []
def product(num):
    for i in xrange(11,21):
        if num%i!=0:
            return 0
    return 1

def minimize(num):
    for k in xrange(20,1,-1):
        if product(num/k) == 1:
            return minimize(num/k)
        elif k==2:
            return num
           
#a = 5
def minprod():
    a=5
    for j in xrange(19,1,-1):
        if product(a) == 1:
            prod.append(a)
            break
        else:
            a = a*j
    new_a = min(prod)
    mini = minimize(new_a)
    return mini


#new_a = min(prod)        
#mini = minimize(new_a)
#print(mini)
#print(time.time()-start)
