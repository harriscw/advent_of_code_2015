#Read data 
text_file = open("../input.txt", "r")
lines = text_file.readlines()[0]

mydict=dict()
currentpos=(0,0) #starting house is origin
mydict[currentpos]=1 #dictionary key is tuple of coordinates, dictionaries can't have lists as keys I guess.  Also starting house gets a gift.  

for i in lines:#iterate over string
	if i =="^":
		currentpos=(currentpos[0],currentpos[1]+1)
	elif i ==">":
		currentpos=(currentpos[0]+1,currentpos[1])
	elif i =="v":
		currentpos=(currentpos[0],currentpos[1]-1)
	elif i =="<":
		currentpos=(currentpos[0]-1,currentpos[1])

	if currentpos in mydict.keys():#give a gift to the current house
		mydict[currentpos]+=1
	else:
		mydict[currentpos]=1
		
print("Final Solution:",len(mydict.keys()))