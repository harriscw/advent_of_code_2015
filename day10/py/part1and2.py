import time

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()

thenum='1321131112'
#thenum='1'

cnt=0
while cnt<50:#40 for part1
	newstring=thenum[0]#initialize new string with first character because loop starts at 2nd position
	for i in range(1,len(thenum)): #this loop creates boundaries for sequences of unique characters
		if thenum[i] != thenum[i-1]: #if this character != previous character
			newstring+="^"+thenum[i] #then insert a character to split on and add it to a growing string
		else: #otherwise just add the character to the growing string
			newstring+=thenum[i]
			
	splitstring=newstring.split("^") #split the resulting string on the split character

	thenum=""
	for substring in splitstring:#get counts per segment and create new string to iterate on
		thenum+=str(substring.count(substring[0]))+str(substring[0])
	cnt+=1
	print(cnt,len(thenum))

print("Start:",start)
print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))