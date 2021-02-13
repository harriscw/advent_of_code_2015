import sys
import itertools
import operator
import time

#Read data 
text_file = open("../input.txt", "r")
lines =[v.strip("\n").replace(",","").replace(":","").split() for v in text_file.readlines()]

mydict=dict() #My initial thought was to get a dictionary keyed by ingredients with values as a dictionary of attributes (flavor=1,texture=2,etc)
for i,line in enumerate(lines): #I later realized that the actual ingredients were not needed
    print(i,line)
    subdict=dict()
    subdict[line[1]]=int(line[2])
    subdict[line[3]]=int(line[4])
    subdict[line[5]]=int(line[6])
    subdict[line[7]]=int(line[8])
    #subdict[line[9]]=int(line[10]) #leave out calories for now
    mydict[line[0]]=subdict

mydict2=dict() #we actually need a list with all values of a given attribute across all ingredients, ie all the "flavors", etc.  Myabe this should have been a matrix and not a dict
mydict2["capacity"]=[mydict[x]["capacity"] for x in mydict.keys()]
mydict2["durability"]=[mydict[x]["durability"] for x in mydict.keys()]
mydict2["flavor"]=[mydict[x]["flavor"] for x in mydict.keys()]
mydict2["texture"]=[mydict[x]["texture"] for x in mydict.keys()]
print(mydict2)

oneto100=list(range(1, 101)) #Get all permutations of 1-100 where length is the number of ingedients
mypermutations=itertools.permutations(oneto100,len(mydict.keys()))
mymax=0

def dotproduct(vec1,vec2): #define a dot product function, stole this from the itertools documentation.  Apparently operator.mul is fast
    return max(0,sum(map(operator.mul, vec1, vec2))) #added max(0,) here according to the puzzle rules
    
start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) #Benchmark
print("Start:",start)
startsec = time.time()

themax=0
for i in itertools.filterfalse(lambda x : sum(x) != 100,mypermutations): #iterate over each permutation but filter to only those that sum to 100
    thismax=1
    for name in mydict2.keys():#for each attribute (ie flavor, texture, etc) get the dot product.  Then multiple the dotproduct of all attributes together
        thismax *= dotproduct(i, mydict2[name])
    if thismax>themax: #if the current number is bigger than the max its the new max
        themax=thismax

print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))
print("Final Answer: ",themax)