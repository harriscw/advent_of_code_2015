var CryptoJS = require("crypto-js");

var startdate = new Date()
secretkey="ckczppom"

cnt=0
stoploop=false
while(stoploop==false){
	cnt+=1
	mystring=secretkey+cnt.toString() //iteratively generate new string
	myhash = CryptoJS.MD5(mystring).toString()
	//console.log(myhash.substring(0,6))
	if(myhash.substring(0,6)=="000000"){
		stoploop=true
	}
}

var enddate = new Date()

console.log('Run Time:', (enddate.getTime() - startdate.getTime())/1000, 'seconds');
console.log(mystring)
console.log(myhash)
console.log("Final Answer:",cnt)