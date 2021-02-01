ret = readlines("../input.txt") #reads as an array

mytotal=0
for (index, value) in enumerate(ret)
	thisdim=map(str -> parse(Int64, str), split(value,"x"))#split string and convert each element of vector to numeric
	
	firstdim=2*thisdim[1] + 2*thisdim[2]
	seconddim=2*thisdim[2] + 2*thisdim[3]
	thirddim=2*thisdim[1] + 2*thisdim[3]
	bow=thisdim[1]*thisdim[2]*thisdim[3]
	
	thisone=(min(firstdim,seconddim,thirddim)+bow)
	global mytotal+=thisone
end

print("Final answer: $mytotal")