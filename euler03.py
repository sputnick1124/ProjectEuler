from sys import argv

if len(argv) > 1:
	num = int(argv[1])
else:
	num = 600851475143
	#num = 13195
x = 2

while num!=1:
    if num%x==0:
        num = num/x
    else:
        x += 1

print(x)
