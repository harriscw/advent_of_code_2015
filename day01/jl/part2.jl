ret = read("input.txt",String)

#print(ret)

thefloor=0
step = 0
for i in 1:length(ret)
	if ret[i]=='('
		global thefloor+=1
	elseif ret[i]==')'
		global thefloor-=1
	end
	global step+=1
	if thefloor==-1
		println("Final answer: $step")
		break
	end
end

