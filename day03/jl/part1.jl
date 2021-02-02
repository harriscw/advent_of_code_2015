ret = read("../input.txt",String)
#print(ret)

mydict=Dict()
currentpos=(0,0) #starting house is origin
mydict[currentpos]=1 #Starting house gets a gift.  

for i in ret #iterate over string
	if i =='^' #Has to be single quotes for some reason...
		global currentpos=(currentpos[1],currentpos[2]+1)
	elseif i =='>'
		global currentpos=(currentpos[1]+1,currentpos[2])
	elseif i =='v'
		global currentpos=(currentpos[1],currentpos[2]-1)
	elseif i =='<'
		global currentpos=(currentpos[1]-1,currentpos[2])
	end
	
	if haskey(mydict,currentpos) #give a gift to the current house
		global mydict[currentpos]+=1
	else
		global mydict[currentpos]=1
	end
end

printstyled("Final Answer: $(length(keys(mydict)))";color=:green)

exit()#Stop!