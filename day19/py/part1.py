import sys

#Read data 
text_file = open("../input.txt", "r")
mylist =[v.strip("\n") for v in text_file.readlines()]

thestring=mylist[-1] #save the molecule
mylist=mylist[:-1]#remove it from the list

oldkey=mylist[0].split(" ")[0] #initialize at first value
mydict=dict() #lets create a dictionary of substitutions
thesevals=[] #initialize empty list of dictionary values
allmols=[]
for line in mylist:
    #print(line.split(" "))
    newkey=line.split(" ")[0] # What is the key for this iteration
    if newkey == oldkey: #if its the same key as last time ...
        thesevals.append(line.split(" ")[-1]) #...then append the substitution to the values
    else: #otherwise if this key is different than last time...
        mydict[oldkey]=thesevals #...write the entry to the dictionary...
        thesevals=[line.split(" ")[-1]] #...and start a new list of values for this key
    oldkey=newkey #reassign oldkey at the end
print(len(list(mydict.keys())),mydict)

#Parse the long molecule string
allmols=list(mydict.keys()) #get a list of all the keys, ie molecules that can be subbed
#allmols.sort(key=lambda s: -len(s)) #sort them by string length, ie H2O ,Mg, H

#Here Im breaking the molecule string into a list
#The general gist of this is to move through each character of the long molecule string
#I look if starting at that position I can find a molecule in my known list of ones that can be subbed
#If I find one I append the start and end positions to a list

pointer=0 #start at the first character
outlist=[] #The list we will build
while pointer <= len(thestring):
    seen=False
    for mol in allmols: #iterate over all known molecules
        #substring from the current position to the current position+length of the current molecule
        if thestring[pointer:pointer+len(mol)]==mol: #if that substring matches the current molecule...
            outlist.append((pointer,pointer+len(mol))) #  ...then append the start and end positions
            pointer+=len(mol) #move the pointer to the end of the molecule you just identified
            seen=True #a flag that you've identified a molecule at the current position
            break #stop looping over molecules
    if seen==False: #if you haven't identified a molecule in your list of subs...
        pointer+=1 #...move to the next position

#Ok now Im going to recreate the entire molecule as a list
#I iterate over the positions in my list of molecules with substitutions and use those to substring the long molecule
#I also substring *between* molecules with subs
#I thought I didn't have to do this at first but apparently it makes a difference

mollist=[thestring[outlist[0][0]:outlist[0][1]]] #start the list with the first molecule
for i in range(1,len(outlist)): #iterate over positions of molecules with substitutions
    thiscoord=outlist[i]
    priorcoord=outlist[i-1]
    mollist.append(thestring[priorcoord[1]:thiscoord[0]]) #append the substring from the end of the prior to start of current
    mollist.append(thestring[thiscoord[0]:thiscoord[1]]) #append this substring (start of current to end of current)
    
mollist=[x for x in mollist if x] #this results in spaces I guess so remove them
newstring=''.join(mollist) #join the list so I can check I did this right
print("Parsed string is the same as the original string:", newstring==thestring)

#Finally, the long molecule is now parsed into a list
#Iterate over it and make substitions if possible
#Append them to a list if they are not already there
themols=[] #the list of molecule we are building
for i in range(len(mollist)): #iterate over each element of the long molecule
    if mollist[i] in mydict.keys(): #If its possible to make a substitution...
        for sub in mydict[mollist[i]]: #...do it iteratively for all possible values
            newlist=mollist.copy() #how am I just learning about this????
            newlist[i]=sub #make the substitution
            thissub=''.join(newlist) #join the list to create a string
            if thissub not in themols: #append if not already there
                themols.append(thissub)

print("Final Answer:",len(themols))