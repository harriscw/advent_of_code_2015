//Read Data
fs  = require("fs");
array = fs.readFileSync("../input.txt").toString().split('\n');
//console.log(array);

mytotal=0
for (i = 0; i < array.length-1; i++) {//for some reason an extra blank element is being picked up
	thisdim=array[i].split("x");
	//console.log(thisdim)
	
	firstdim=parseInt(thisdim[0])*parseInt(thisdim[1])
	seconddim=parseInt(thisdim[1])*parseInt(thisdim[2])
	thirddim=parseInt(thisdim[0])*parseInt(thisdim[2])
	minall=Math.min(firstdim,seconddim,thirddim)
	thisone=(2*firstdim+2*seconddim+2*thirddim+minall)
	
	mytotal+=thisone
}	

console.log("Final:",mytotal)