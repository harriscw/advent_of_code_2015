import re
import sys

#Read data 
text_file = open("../input.txt", "r")
lines =[v.strip("\n") for v in text_file.readlines()]

#lines=["ugknbfddgicrmopn","aaa","jchzalrnumimnmhp","haegwjzuvuyypxyu","dvszwmarrgswjxmb"]

doubles = re.compile(r"(.)\1") #regex for repeating characters
badstrings = re.compile('ab|cd|pq|xy') #regex for forbidden strings
nicestrings=0 #initialize counter for nice strings

for line in lines:

	#Get vowel count
	vowelcnt=0
	for letter in line:
		if letter in ['a','e','i','o','u']:
			vowelcnt+=1
	
	# Does it have doubles
	hasdoubles=re.search(doubles, line)!=None
	
	# Does it have a forbidden string
	hasbadstring=badstrings.search(line)!=None
	
	#print(line,vowelcnt,hasdoubles,hasbadstring)
	if vowelcnt>=3 and hasdoubles==True and hasbadstring==False:
		nicestrings+=1

print("Keepers:",nicestrings)