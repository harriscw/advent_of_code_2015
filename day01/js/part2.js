//Read Data
fs  = require("fs");
array = fs.readFileSync("input.txt").toString();
//console.log(array);

floor=0
step=0
for (i = 0; i < array.length; i++) {
	if(array[i]=="("){
		floor+=1
	}
	else if(array[i]==")"){
		floor-=1
	}
	step+=1
	if(floor==-1){
		console.log(step)
		break
	}
	}

