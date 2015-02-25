import time
start = time.time()
ones = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
tens = ['','','twen','thir','for','fif',ones[6],ones[7],'eigh',ones[9],'teen','ty']
misc = ['hundred','thousand','and']

st = 0
for y in range(10):
    if y==0:
        c = 0
    else:
        c = 1
    st += len(ones[y]+misc[0]*c)
##    print(ones[y]+misc[0]*c)
    for x in range(1,100):
        if x<=12:
            st += len(ones[y]+misc[0]*c+misc[-1]*c+ones[x])
##            print(ones[y]+misc[0]*c+misc[-1]*c+ones[x])
        else:
            if str(x)[0]=='1':
                if int(str(x)[1])==4:
                    st += len(ones[y]+misc[0]*c+misc[-1]*c+ones[int(str(x)[1])]+tens[-2])
##                    print(ones[y]+misc[0]*c+misc[-1]*c+ones[int(str(x)[1])]+tens[-2])
                else:
                    st += len(ones[y]+misc[0]*c+misc[-1]*c+tens[x-10]+tens[-2])
##                    print(ones[y]+misc[0]*c+misc[-1]*c+tens[x-10]+tens[-2])
            else:
                st += len(ones[y]+misc[0]*c+misc[-1]*c+tens[int(str(x)[0])]+tens[-1]+ones[int(str(x)[1])])
##                print(ones[y]+misc[0]*c+misc[-1]*c+tens[int(str(x)[0])]+tens[-1]+ones[int(str(x)[1])])
st += len(ones[1]+misc[1])
##print(ones[1]+misc[1])
print(time.time()-start)
