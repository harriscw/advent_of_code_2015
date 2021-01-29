#Read data 
text_file = open("../input.txt", "r")
lines = text_file.readlines()

#lines=["2x3x4","1x1x10"]

mytotal=0
for line in lines:
	thisdim=list(map(int,line.strip("\n").split("x")))
	firstdim=thisdim[0]*thisdim[1]
	seconddim=thisdim[1]*thisdim[2]
	thirddim=thisdim[0]*thisdim[2]
	minall=min(firstdim,seconddim,thirddim)
	thisone=(2*firstdim+2*seconddim+2*thirddim+minall)
	#print(firstdim,seconddim,thirddim,minall,thisone)
	mytotal+=thisone
	

print("Final:",mytotal)