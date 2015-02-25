print(sum([x for x in range(1,1000000,2) if str(x)==str(x)[::-1] and bin(x)[2:]==bin(x)[2:][::-1]]))
