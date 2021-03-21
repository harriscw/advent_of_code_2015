import sys

thenum=9
thenum=34000000
testnum=100000

#mydict={el:0 for el in range(1,thenum+1)}
#print(mydict)
mydict=dict()
for elf in range(1,testnum+1):
    if elf % 100==0:
        print(elf)
    elfcnt=0
    for housenum in range(1,testnum+1):
        if (housenum % elf ==0):
            elfcnt+=1
            if housenum in mydict.keys():
                mydict[housenum]+=elfcnt*10
            else:
                mydict[housenum]=elfcnt*10
            if mydict[housenum]>=thenum:
                print("Final Answer:",housenum,mydict[housenum])
                sys.exit()

print(mydict)