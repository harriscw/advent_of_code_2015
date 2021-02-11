import sys
import itertools

#Read data 
text_file = open("../input.txt", "r")
lines =[v.strip("\n").strip(".").split() for v in text_file.readlines()]

mydict=dict()
for i,line in enumerate(lines):#create a dictionary where each person is a unique key and value is a dictionary with key=person, value=happiness score
	#print(line[0],line[2],line[3],line[-1])
	if line[2]=="gain":#get sign for happiness score
		posneg=1
	else:
		posneg=-1
	if line[0] not in mydict:#if the key isn't in the dictionary yet create one with a blank dict as a value
		mydict[line[0]]=dict()
	mydict[line[0]][line[-1]]=posneg*int(line[3])#add to the dictionary

names=list(mydict.keys())
#print(names)
#print(mydict)

happinesses=[]
for combo in itertools.permutations(names, len(names)):# iterate over all permutations of seating arrangements
	#print(combo)
	thesum=mydict[combo[-1]][combo[0]]+mydict[combo[0]][combo[-1]]#get happiness for this arrangement.  Initalize to happiness combo for first and last people in this permutation
	for j in range(len(combo)-1):#iterate over the seating arrangement
		thesum+=mydict[combo[j]][combo[j+1]]+mydict[combo[j+1]][combo[j]]
	happinesses.append(thesum)
print("Final Answer:",max(happinesses))