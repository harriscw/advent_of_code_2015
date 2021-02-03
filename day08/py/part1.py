import sys

#Read data 
text_file = open("../input.txt", "r")
lines =[v.strip("\n") for v in text_file.readlines()]
#print(lines)

rawcnt=rescnt=0
for line in lines:
	rawline=line.encode('unicode-escape').decode() 
	resline=line.encode('utf-8').decode('unicode_escape') #https://stackoverflow.com/questions/2428117/casting-raw-strings-python
	
	print(rawline,len(rawline))
	print(resline,len(resline))
		
	rawcnt+=len(rawline)-rawline.count("\\")/2 #This method for getting raw string adds a \, so I subtract 1 for every \ in the string
	rescnt+=len(resline)-2 #Subtract 2 every string for the double quotes which aren't getting evaluated

print(rawcnt,"-",rescnt,"=",rawcnt-rescnt)