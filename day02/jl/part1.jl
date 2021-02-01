ret = readlines("../input.txt") #reads as an array

mytotal=0
for (index, value) in enumerate(ret)
	thisdim=map(str -> parse(Int64, str), split(value,"x"))#split string and convert each element of vector to numeric
	
	firstdim=thisdim[1]*thisdim[2]
	seconddim=thisdim[2]*thisdim[3]
	thirddim=thisdim[1]*thisdim[3]
	
	minall=min(firstdim,seconddim,thirddim)
	thisone=(2*firstdim+2*seconddim+2*thirddim+minall)
	global mytotal+=thisone
end

print("Final answer: $mytotal")