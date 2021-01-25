#Read data 
text_file = open("../input.txt", "r")
lines = text_file.readlines()

mytotal=0
for line in lines:
	thisdim=list(map(int,line.strip("\n").split("x")))
	firstdim=2*thisdim[0]*thisdim[1]
	seconddim=2*thisdim[1]*thisdim[2]
	thirddim=2*thisdim[0]*thisdim[1]
	minall=min(firstdim,seconddim,thirddim)
	mytotal+=(firstdim+seconddim+thirddim+minall)

print("Final:",mytotal)