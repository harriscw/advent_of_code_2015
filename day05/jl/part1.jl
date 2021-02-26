ret = split(read("../input.txt",String),"\n")
#ret=["ugknbfddgicrmopn","aaa","jchzalrnumimnmhp","haegwjzuvuyypxyu","dvszwmarrgswjxmb"]

doubles =r"(.)\1"
badstrings=r"ab|cd|pq|xy"

nicestrings=0
for (index, line) in enumerate(ret)
	#Get vowel count
	global vowelcnt=0
	for letter in line
		if string(letter) in ["a","e","i","o","u"]
			global vowelcnt+=1
		end
	end

	global hasdoubles = match(doubles, string(line)) != nothing
	global hasbadstring = match(badstrings, string(line)) != nothing

	println("$line $vowelcnt $hasdoubles $hasbadstring")

	if vowelcnt>=3 && hasdoubles==true && hasbadstring==false #Single & gives the wrong answer!
		global nicestrings+=1
	end
end

print("Final answer: $nicestrings")


