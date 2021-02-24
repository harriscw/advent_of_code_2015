import sys
import itertools

#Read data 
text_file = open("../input.txt", "r")
lines =[int(v.strip("\n")) for v in text_file.readlines()]

outlist=[] #create an empty list to append to
for thelength in range(1,len(lines)+1): #iterate over different possible lengths
    for combo in itertools.combinations(lines,thelength): #iterate over all combinations at the given length
        if sum(combo) ==150: #if it sums to 150 then append to the list
            outlist.append(combo)

print("Final Answer:",len(outlist)) #Part 1 answer

themin=min([len(x) for x in outlist])
acc=0
for sublist in outlist:
    if len(sublist)==themin:
        acc+=1

print("Final Answer:",acc) #Part 2 answer