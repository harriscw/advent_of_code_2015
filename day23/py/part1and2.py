import sys

text_file = open("../input.txt", "r")
instrux =[v.strip("\n") for v in text_file.readlines()]

instruxlist=[] # parse instructions into a list of lists
for instruction in instrux:
    mysplit=instruction.replace(",","").split(" ")
    if mysplit[0] in ["jmp","jie","jio"]: #set the last part of the instruction to integer for these guys
        mysplit[-1]=int(mysplit[-1])
    instruxlist.append(mysplit)

def doit(astart):
    mydict=dict()
    mydict['a']=astart 
    mydict['b']=0 
    counter=0
    while counter<len(instruxlist): #keep iterating until you get to a point past your instructions
        thisinstrux=instruxlist[counter]
        if thisinstrux[0]=="hlf":
            mydict[thisinstrux[-1]]=0.5*mydict[thisinstrux[-1]]
            counter+=1
        elif thisinstrux[0]=="tpl":
            mydict[thisinstrux[-1]]=3.0*mydict[thisinstrux[-1]]
            counter+=1
        elif thisinstrux[0]=="inc":
            mydict[thisinstrux[-1]]+=1
            counter+=1
        elif thisinstrux[0]=="jmp":
            counter+=thisinstrux[-1]
        elif thisinstrux[0]=="jie":
            if mydict[thisinstrux[1]] % 2 == 0:
                counter+=thisinstrux[-1]
            else:
                counter+=1
        elif thisinstrux[0]=="jio":
            if mydict[thisinstrux[1]]==1:
                counter+=thisinstrux[-1]
            else:
                counter+=1
    return("a:",mydict['a'],"b:",mydict['b'])

print("Part 1: ",doit(astart=0))
print("Part 2: ",doit(astart=1))