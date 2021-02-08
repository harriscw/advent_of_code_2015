import sys
import itertools
import time

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) #start the clock
startsec = time.time()

myinput="vzbxkghb" #part1
myinput="vzbxxyzz" #part2

alphabet='abcdefghijklmnopqrstuvwxyz'

straights=[]#get all 3 letter straights in the alphabet
for i in range(3,len(alphabet)+1):
	straights.append(alphabet[i-3:i])

def checkstring(string):#see if a string meets all the conditions
	#print(string)
	if any(x in string for x in ["i","o","l"]):#Check for forbidden characters
		return False
	elif not any(x in string for x in straights):#Check for 3 letter straights
		return False
	else: #Check for multiple consecutive letters
		checklist=[]
		for sublist in [[k, len(list(g))] for k, g in itertools.groupby(string)]:#https://stackoverflow.com/questions/13197668/counting-consecutive-characters-in-a-string
			if sublist[1]>1:#append all repeats
				checklist.append(sublist[0])
		if len(checklist)<=1:#Reject if not 2+ repeats
			return False
		else:
			return True

SUCC = {a: b for a, b in zip(alphabet, alphabet[1:] + "a")} #This code sets up the odometer.  I stole it almost verbatim
def odo_inc(data): #https://programmingpraxis.com/2018/08/03/odometer/
    datalist = list(data)
    for j, c in reversed(list(enumerate(datalist))):
        datalist[j] = succ = SUCC[c]
        if succ not in "a":
            break
    return "".join(datalist)

cnt=0
string=myinput
while True:
	string=odo_inc(data=string) #increment string
	#print(string)
	mycheck=checkstring(string) #Check if its valid
	if mycheck==True: #if its valid then break
		print("Final Answer:",string,cnt)
		break
	cnt+=1

print("Start:",start)
print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))