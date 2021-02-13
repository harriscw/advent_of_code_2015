import sys

#Read data 
text_file = open("../input.txt", "r")
lines =[v.strip("\n").replace(",","").replace(":","").split() for v in text_file.readlines()]

mydict=dict() #make a dictionary where key is Sue number and values are a dictionary of Sue attributes
for i,line in enumerate(lines): 
    #print(i,line)
    subdict=dict() #create sub dictionary of attributes
    for j in range(2,len(line),2):#iterate every other starting after Sue number
        subdict[line[j]]=int(line[j+1])
    mydict[int(line[1])]=subdict

print(mydict)

thesue={ #dictionary of the real Sue
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}

plausiblesues=[] #initialize list of plausible Sues
for thissue in mydict.keys(): #iterate over Sue number
    appendit=True
    for myattrib in mydict[thissue].keys(): #iterate over known attributes of current Sue
        if mydict[thissue][myattrib]!=thesue[myattrib]: #if its not equal to the real Sue's attributes then don't append
            appendit=False
            break
    if appendit==True:#otherwise do append
        plausiblesues.append(thissue)

print("Final Answer:",plausiblesues)