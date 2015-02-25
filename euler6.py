n = 100
sumsq=[]
sqsum=[]
for x in range(1,n+1):
    sumsq.append(x**2)
    sqsum.append(x)
diff = sum(sqsum)**2-sum(sumsq)
print(diff)
