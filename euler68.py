from time import time
from itertools import permutations as perms
from copy import copy

t1=time()
b=list([x for x in perms(range(1,11),3) if sum(x)==y and x[0]>5 and max(x[1:])<6] for y in range(13,20))
fams={}
c1,c2,c3,c4,c5=0,0,0,0,0
for a in b:
    for parent in a:
        if parent[0]!=6:
            continue
        for child1 in a:
            test1={parent[0]}
            if child1[1]==parent[2] and child1[0] not in test1:
                test2=copy(test1)
                test2.add(child1[0])
                for child2 in a:
                    if child2[1]==child1[2] and child2[0] not in test2:
                        test3=copy(test2)
                        test3.add(child2[0])
                        for child3 in a:
                            if child3[1]==child2[2] and child3[0] not in test3:
                                test4=copy(test3)
                                test4.add(child3[0])
                                for child4 in a:
                                    if child4[1]==child3[2] and child4[0] not in test4:
                                        if child4[2]==parent[1]:
                                            fams[parent]=[parent,child1,child2,child3,child4]
print(''.join([str(x) for sub in max(fams.values()) for x in sub]))
print(time()-t1)

