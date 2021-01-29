#Read data 
text_file = open("../input.txt", "r")
lines = text_file.readlines()

#lines=["2x3x4","1x1x10"]

mytotal=0
for line in lines:
	thisdim=list(map(int,line.strip("\n").split("x")))
	firstdim=2*thisdim[0] + 2*thisdim[1]
	seconddim=2*thisdim[1] + 2*thisdim[2]
	thirddim=2*thisdim[0] + 2*thisdim[2]
	bow=thisdim[0]*thisdim[1]*thisdim[2]
	
	thisone=(min(firstdim,seconddim,thirddim)+bow)
	#print(firstdim,seconddim,thirddim,bow,thisone)
	mytotal+=thisone
	
print("Final:",mytotal)