ret = read("input.txt",String)

#print(ret)

thefloor=0
for i in 1:length(ret)
	if ret[i]=='('
		global thefloor+=1
	elseif ret[i]==')'
		global thefloor-=1
	end
end

println("Final answer: $thefloor")