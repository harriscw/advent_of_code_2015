import sys
#Read data 
text_file = open("../input0.txt", "r")
lines =[v.strip("\n") for v in text_file.readlines()]
#print(lines)

rawcnt=enccnt=0
for line in lines:
	rawline=line.encode('unicode-escape').decode()
	
	thisraw=len(rawline)-rawline.count("\\")/2 #This is just the same as part 1 I believe
	thisenc=len(rawline)+4 #All backslashes are counted now.  Add an extra 4 because each " adds and extra \" apparently and there's at least 2 " per string.
	if rawline.count('\"')>2: #Apparently \" becomes to \\" so add 1 for each " on top of the outer "" every string has
		thisenc+=rawline.count('\"')-2
	
	print(rawline,thisraw,thisenc,rawline.count('\"'))
	
	rawcnt+=thisraw
	enccnt+=thisenc

print(enccnt,"-",rawcnt,"=",enccnt-rawcnt)