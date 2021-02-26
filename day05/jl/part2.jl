ret = split(read("../input.txt",String),"\n")
#ret=["ugknbfddgicrmopn","aaa","jchzalrnumimnmhp","haegwjzuvuyypxyu","dvszwmarrgswjxmb"]

twocharsrepeat = r"\b\w*(\w{2})\w*\1"

nicestrings=0
for (index, line) in enumerate(ret)
	global cond1 = match(twocharsrepeat, string(line)) != nothing

	global cond2=false
	theline=string(line)
	for i=3:length(theline)
		if theline[i]==theline[i-2]
			global cond2=true
			break
		end
	end

	if cond1==true && cond2==true
		global nicestrings+=1
	end
end

print("Final answer: $nicestrings")

exit()