#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()

mystring=lines[0]
thefloor=0
step=0
for i in range(len(mystring)):
	if mystring[i]=="(":
		thefloor+=1
	elif mystring[i]==")":
		thefloor-=1
	step+=1
	if thefloor==-1:
		print("Final Answer:",step)
		break

