#Read data 
text_file = open("../input.txt", "r")
lines = text_file.readlines()[0]

mydict=dict()
santapos=(0,0) #santa start position
robopos=(0,0) #robot start position
mydict[(0,0)]=1 #dictionary key is tuple of coordinates, dictionaries can't have lists as keys I guess.  Also starting house gets a gift.  

def updatepos(i,currentpos):
	if i =="^":
		currentpos=(currentpos[0],currentpos[1]+1)
	elif i ==">":
		currentpos=(currentpos[0]+1,currentpos[1])
	elif i =="v":
		currentpos=(currentpos[0],currentpos[1]-1)
	elif i =="<":
		currentpos=(currentpos[0]-1,currentpos[1])
	return(currentpos)
	
def updatedict(currentpos,mydict):
	if currentpos in mydict.keys():#give a gift to the current house
		mydict[currentpos]+=1
	else:
		mydict[currentpos]=1
	return(mydict)

cnt=1	
for i in lines:#iterate over string
	if cnt % 2:#odd
		santapos=updatepos(i=i,currentpos=santapos)
		mydict=updatedict(currentpos=santapos,mydict=mydict)
	else:#even
		robopos=updatepos(i=i,currentpos=robopos)
		mydict=updatedict(currentpos=robopos,mydict=mydict)
	cnt+=1

print("Final Solution:",len(mydict.keys()))