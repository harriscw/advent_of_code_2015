import re

#Read data 
text_file = open("../input.txt", "r")
lines =[v.strip("\n") for v in text_file.readlines()]

#lines=["qjhvhtzxzqqjkmpb","xxyxx","uurcxstgmygtbstg","ieodomkazucvgmuy"]

twocharsrepeat = re.compile(r"\b\w*(\w{2})\w*\1") #regex for two characters that repeat somewhere in the strings, got this verbatim from stack overflow
#https://stackoverflow.com/questions/15600053/regex-words-with-two-letters-repeated-twice-eg-abpoiuyab-xnvxylsdjsdxymsd

nicestrings=0 #initialize counter for nice strings
for line in lines:
	print(line)
	
	cond1=len(re.findall(twocharsrepeat, line))>0# Find strings where two characters repeat somewhere
	
	cond2=False
	for i in range(2,len(line)):# look for 2 characters separated by a character, e.g. xyx.  Couldnt find/think of a regex
		if line[i]==line[i-2]:
			cond2=True
			break
			#print("Got one!",line[i-2:i+1])
	if cond1==True and cond2==True:
		nicestrings+=1

print("Keepers:",nicestrings)