import sys
import re

#Read data 
text_file = open("../input.txt", "r")
lines = text_file.readlines()[0]
#lines="[1,2,3]"
#lines="[1,{\"c\":\"red\",\"b\":2},3]"
#lines="{\"d\":\"red\",\"e\":[1,2,3,4],\"f\":5}"
#lines="[1,\"red\",5]"

#My strategy here is to identify all dictionaries containing "red", zero them out, then apply my solution from the first problem

thereds=dict()
for i in range(5,len(lines)): #iterate over each character in the string
	if lines[i-5:i]==":\"red": #look for dictionary attribute indicating red
		#print(lines[i-5:i])
				
		#So now you have to identify the dictionary {} portion in the string the 'red' is a part of
		priorstringrev=lines[:i-5][::-1] #First get the string prior to the 'red' and reverse it
		cnta=0
		for j in range(len(priorstringrev)):#iterate backwards through the prior string to find the first unmatched {
			#print(cnta,j,priorstringrev[j])
			if priorstringrev[j]=="{" and cnta==0:#This part is a rigmarole to account for {s that are paired with a } you already saw
				priorindex=len(priorstringrev)-j-1
				break
			elif priorstringrev[j]=="}":
				cnta+=1
			elif priorstringrev[j]=="{":
				cnta-=1
		#print("prior index:",priorindex,lines[priorindex])		

		nextstring=lines[i:]#Now do the same thing to find the first unmatched } in the string after the red
		cntb=0
		for j in range(len(nextstring)):
			#print(cntb,j,nextstring[j])
			if nextstring[j]=="}" and cntb==0:
				nextindex=i+j
				break
			elif nextstring[j]=="{":
				cntb+=1
			elif nextstring[j]=="}":
				cntb-=1
		#print("next index:",nextindex,lines[nextindex])
		
		print("found red at position:",str(i)+", region to zero out: ["+str(priorindex)+","+str(nextindex)+"]")
		thereds[i-5]=(priorindex,nextindex)#add the dictionary indicies to a dictionary indexed by the "red" index

finallist= sorted(list(set(thereds.values())), key=lambda x: x[0]) #get unique regions to splice and sort

print(finallist)
print("length final list:",len(finallist))

for theposition in finallist: #now zero out these regions by changing them to a string with no number.
	spliceout=lines[theposition[0]:theposition[1]+1] #this is the region that will be removed
	splicein="X"*len(spliceout) #replace it with a string of Xs of equal length
	#print("XXX",cnt,len(spliceout),len(splicein),spliceout)
	#print("Pre-splice length:",len(lines))
	lines=lines[:theposition[0]]+splicein+lines[theposition[1]+1:] #perform the splice
	#print("Post-splice length:",len(lines))

print("Post-splice:",lines)

mylist=[int(x) for x in re.findall(r'-?\d+', lines)] #apply part 1 solution
print("Final Answer:",sum(mylist))