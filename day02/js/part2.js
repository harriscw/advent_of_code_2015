//Read Data
fs  = require("fs");
array = fs.readFileSync("../input.txt").toString().split('\n');
//console.log(array);

mytotal=0
for (i = 0; i < array.length-1; i++) {//for some reason an extra blank element is being picked up
	thisdim=array[i].split("x");
	//console.log(thisdim)
	
	firstdim=2*parseInt(thisdim[0])+2*parseInt(thisdim[1])
	seconddim=2*parseInt(thisdim[1])+2*parseInt(thisdim[2])
	thirddim=2*parseInt(thisdim[0])+2*parseInt(thisdim[2])
	bow=thisdim[0]*thisdim[1]*thisdim[2]
	thisone=(Math.min(firstdim,seconddim,thirddim)+bow)
	
	mytotal+=thisone
}	

console.log("Final:",mytotal)