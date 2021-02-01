import sys

def bit_not(n, numbits=16): #https://stackoverflow.com/questions/31151107/how-do-i-do-a-bitwise-not-operation-in-python
    return (1 << numbits) - 1 - n
	
def is_int(val):#check if string can be converted to integer
    try:
        num = int(val)
    except ValueError:
        return False
    return True

#Read data 
text_file = open("../input.txt", "r")
lines =[v.strip("\n") for v in text_file.readlines()]

instrux=dict()#Get a dictionary of all the unique assignments/keys
for i,line in enumerate(lines):
	thesplit=line.split(" -> ")
	instrux[thesplit[-1]]=thesplit[0]

seen=[] #Get an initial list of instructions starting with instructions where a numeric value only is assigned
for i,line in enumerate(lines):
	if any(x in line for x in ["AND","OR","SHIFT","NOT"]):
		continue
	else:
		mysplit=line.split(" -> ")
		try:
			int(mysplit[0])
			seen.append(line)
		except ValueError:
			print("Nope:",mysplit[0])

oldlen=len(seen) #Now order the rest of the instructions
while len(seen)<len(instrux.keys()):#go until you've ordered everything
	oldlen=len(seen)
	knownkeys=[x.split(" -> ")[-1] for x in seen]#get all the current known keys
	print("Ordering Instructions:",str(len(seen))+"/"+str(len(lines)))
	for line in lines:#iterate over all instructions
		if line not in seen: #if you haven't seen this instruction before then get all keys needed to execute this instruction
			lhs = line.split(" -> ")[0] #get only left hand side part
			neededkeys=lhs.replace(" AND ",";").replace(" OR ",";").replace(" LSHIFT ",";").replace(" RSHIFT ",";").replace("NOT ",";").split(";") #get unique keys
			neededkeys=list(filter(None,neededkeys)) #filter empty elements
			removeitem=""
			for mykey in neededkeys: #rigamarole to remove integers among keys
				try:
					int(mykey)
					removeitem=mykey
				except ValueError:
					continue
			if removeitem in neededkeys: 
				neededkeys.remove(removeitem)
			if all(x in knownkeys for x in neededkeys):#if all need keys are in known keys
				seen.append(line)

print("Final Ordered Instructions:",str(len(seen))+"/"+str(len(lines)))
print("Dups:",list(set([x for x in seen if seen.count(x) > 1])))

#Now execute each instruction
mydict=dict()
for i,line in enumerate(seen):
	line=line.split(" -> ")
	if "AND" in line[0]:
		myleft=line[0].split(" AND ")[0]
		myright=line[0].split(" AND ")[-1]
		if is_int(myleft):
			theleft=int(myleft)#use the integer val
		else:
			theleft=mydict[myleft]#use the value at the dictionary location
		if is_int(myright):
			theright=int(myright)
		else:
			theright=mydict[myright]
		mydict[line[-1]]=theleft & theright
	elif "OR" in line[0]:
		myleft=line[0].split(" OR ")[0]
		myright=line[0].split(" OR ")[-1]
		if is_int(myleft):
			theleft=int(myleft)#use the integer val
		else:
			theleft=mydict[myleft]#use the value at the dictionary location
		if is_int(myright):
			theright=int(myright)
		else:
			theright=mydict[myright]
		mydict[line[-1]]=theleft | theright
	elif "LSHIFT" in line[0]:
		myleft=line[0].split(" LSHIFT ")[0]
		myright=line[0].split(" LSHIFT ")[-1]
		if is_int(myleft):
			theleft=int(myleft)#use the integer val
		else:
			theleft=mydict[myleft]#use the value at the dictionary location
		if is_int(myright):
			theright=int(myright)
		else:
			theright=mydict[myright]
		mydict[line[-1]]=theleft << theright
	elif "RSHIFT" in line[0]:
		myleft=line[0].split(" RSHIFT ")[0]
		myright=line[0].split(" RSHIFT ")[-1]
		if is_int(myleft):
			theleft=int(myleft)#use the integer val
		else:
			theleft=mydict[myleft]#use the value at the dictionary location
		if is_int(myright):
			theright=int(myright)
		else:
			theright=mydict[myright]
		mydict[line[-1]]=theleft >> theright
	elif "NOT" in line[0]:
		mystring=line[0].replace("NOT ","")
		if is_int(mystring):
			myval=int(mystring) #use the integer val
		else:
			myval=mydict[mystring]#use the value at the dictionary location
		mydict[line[-1]]=bit_not(myval)
	else:
		if is_int(line[0]):
			myval=int(line[0])
		else:
			myval=mydict[line[0]]
		mydict[line[-1]]=myval
	
print("Final Answer:",mydict["a"])