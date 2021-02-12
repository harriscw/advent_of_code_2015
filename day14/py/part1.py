import sys

#Read data 
text_file = open("../input.txt", "r")
lines =[v.strip("\n").strip(".").split() for v in text_file.readlines()]

mydict=dict()
for line in lines: #create a dictionary where key is each reindeer
    #print(line[0],line[3],line[6],line[-2])
    subdict=dict()
    subdict["distance"]=int(line[3])
    subdict["duration"]=int(line[6])
    subdict["rest"]=int(line[-2])
    mydict[line[0]]=subdict

#print(mydict)

def getposition(reindeer,seconds):#For a given reindeer, find the final position after a given amount of seconds
    cnt=1
    thesum=0
    for i in range(seconds+1): #iterate over number of seconds
        #print(i,cnt,thesum)
        if cnt<=mydict[reindeer]["duration"]: #if the counter is < duration the reindeer flys for then add the amount it traveled.  Otherwise nothing will happen
            thesum+=mydict[reindeer]["distance"]
        elif cnt==mydict[reindeer]["duration"]+mydict[reindeer]["rest"]:#If the counter hits the duration+rest time then reset it to 0
            cnt=0
        cnt+=1
    return(thesum)

# print(getposition("Comet",seconds=1000))
# print(getposition("Dancer",seconds=1000))

def doit(secs):
    theposition=[]
    for name in mydict.keys():#iterate over each reindeer to see where it will be after X seconds
        print(name,getposition(name,seconds=secs))
        theposition.append(getposition(name,seconds=secs))

    return(max(theposition))
print("Final Answer:",doit(2503))
#2585 too low
#3762 too high