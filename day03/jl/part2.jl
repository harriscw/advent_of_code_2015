ret = read("../input.txt",String)
#print(ret)

mydict=Dict()
santapos=(0,0) #starting house is origin
robopos=(0,0) #starting house is origin
mydict[(0,0)]=1 #Starting house gets a gift. 

function updatepos(;j,currentpos) #Note semi colon!!!
	if j =='^'
		currentpos=(currentpos[1],currentpos[2]+1)
	elseif j =='>'
		currentpos=(currentpos[1]+1,currentpos[2])
	elseif j =='v'
		currentpos=(currentpos[1],currentpos[2]-1)
	elseif j =='<'
		currentpos=(currentpos[1]-1,currentpos[2])
	end
	return currentpos
end

function updatedict(;currentpos,mydict) #Note semi colon!!!
	if haskey(mydict,currentpos)#give a gift to the current house
		mydict[currentpos]+=1
	else
		mydict[currentpos]=1
	end
	return mydict
end

cnt=1	
for i in ret #iterate over string
	if isodd(cnt) #odd
		global santapos=updatepos(j=i,currentpos=santapos)
		global mydict=updatedict(currentpos=santapos,mydict=mydict)
	else #even
		global robopos=updatepos(j=i,currentpos=robopos)
		global mydict=updatedict(currentpos=robopos,mydict=mydict)
	end
	global cnt+=1
end	

printstyled("Final Answer: $(length(keys(mydict)))";color=:green)

exit()