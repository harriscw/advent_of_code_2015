//Read Data
fs  = require("fs");
array = fs.readFileSync("../input.txt").toString();

mydict={}
currentpos=[0,0] //starting house is origin
mydict[currentpos]=1 //starting house gets a gift.  

for (i = 0; i < array.length; i++) {//iterate over string

	if(array[i] =="^"){currentpos=[currentpos[0],currentpos[1]+1]}
	else if(array[i] ==">"){currentpos=[currentpos[0]+1,currentpos[1]]}
	else if(array[i] =="v"){currentpos=[currentpos[0],currentpos[1]-1]}
	else if(array[i] =="<"){currentpos=[currentpos[0]-1,currentpos[1]]}

	if(currentpos in Object.keys(mydict)){//give a gift to the current house
		mydict[currentpos]+=1
	}
	else{
		mydict[currentpos]=1
	}
}

console.log("Final Answer:",Object.keys(mydict).length)
