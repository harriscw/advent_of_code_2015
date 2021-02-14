using MD5
using Dates

starttime=now()
secretkey="ckczppom"

cnt=0
stoploop=false
while stoploop==false
	global cnt+=1
	global mystring=secretkey*string(cnt) #iteratively generate new string
	global myhash=bytes2hex(md5(mystring)) #get the md5 hash
	if myhash[1:6]=="000000"
		global stoploop=true
    end
end

println("Run Time: $((now()-starttime).value/1000) seconds")
println(mystring)
println(myhash)
println("Final Answer:",cnt)


exit()#Stop!