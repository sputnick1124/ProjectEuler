
from math import factorial as fact

print(sum(x for x in range(3,50000) if sum(fact(int(y)) for y in str(x))==x))

