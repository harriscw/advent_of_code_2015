//Read Data
fs  = require("fs");
array = fs.readFileSync("../input.txt").toString();

santapos=robotpos=[0,0] //starting house is origin
mydict={}
mydict[[0,0]]=1 //starting house gets a gift.  

function updatepos(i, currentpos) {
	if(array[i] =="^"){currentpos=[currentpos[0],currentpos[1]+1]}
	else if(array[i] ==">"){currentpos=[currentpos[0]+1,currentpos[1]]}
	else if(array[i] =="v"){currentpos=[currentpos[0],currentpos[1]-1]}
	else if(array[i] =="<"){currentpos=[currentpos[0]-1,currentpos[1]]}
	return currentpos
  }

cnt=1
for (i = 0; i < array.length; i++) {//iterate over string

	if(cnt % 2){
		santapos=updatepos(i=i,currentpos=santapos)
		if(santapos in Object.keys(mydict)){//give a gift to the current house.  Couldn't get Object.keys(mydict) to work inside a function for some reason.
			mydict[currentpos]+=1 //I had a parameter called mydict in addition to the global object.  Got the error: Cannot convert undefined or null to object
		}
		else{
			mydict[currentpos]=1
		}
	}
	else{
		robotpos=updatepos(i=i,currentpos=robotpos)
		if(robotpos in Object.keys(mydict)){//give a gift to the current house
			mydict[currentpos]+=1
		}
		else{
			mydict[currentpos]=1
		}
	}
	cnt+=1
}

console.log("Final Answer:",Object.keys(mydict).length)