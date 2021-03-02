ret = split(read("../input.txt",String),"\n")

instrux=[]
for (index, line) in enumerate(ret)
    newlist=split(line," ")
    if newlist[1]=="toggle"
		global instruct="toggle"
        global lowerrow=parse(Int64,split(newlist[2],",")[1])
		global lowercol=parse(Int64,split(newlist[2],",")[2])
    else
        instruct=newlist[2]
        global lowerrow=parse(Int64,split(newlist[3],",")[1])
		global lowercol=parse(Int64,split(newlist[3],",")[2])
    end
    global upperrow=parse(Int64,split(last(newlist),",")[1])
    global uppercol=parse(Int64,split(last(newlist),",")[2])
    push!(instrux, [instruct, lowerrow, lowercol, upperrow, uppercol])
end

mygrid = zeros(Int64,1000,1000)

for instruction in instrux #execute the instructions
	if instruction[1]=="on"
		for row in instruction[2]:instruction[4] #switch on
			for col in instruction[3]:instruction[5]
				global mygrid[row,col]+=1
            end
        end
    elseif instruction[1]=="off"
        for row in instruction[2]:instruction[4] #switch off
            for col in instruction[3]:instruction[5]
                global mygrid[row,col]=max(0,mygrid[row,col]-1)
            end
        end
    else
        for row in instruction[2]:instruction[4] #toggle
            for col in instruction[3]:instruction[5]
                mygrid[row,col]+=2
            end
        end
    end
end
println("Final Answer: ",sum(mygrid))