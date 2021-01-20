#Read data 
text_file = open("input.txt", "r")
lines = text_file.readlines()

mystring=lines[0]
mylist=[]
for i in range(len(mystring)):
	if mystring[i]=="(":
		mylist.append(1)
	elif mystring[i]==")":
		mylist.append(-1)

print("Final Answer:",sum(mylist))