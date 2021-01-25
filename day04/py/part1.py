import hashlib

secretkey="ckczppom"
#secretkey="abcdef"
cnt=0
stoploop=False
while stoploop==False:
	mystring=secretkey+str(cnt)
	myhash=hashlib.md5(mystring.encode("utf")).hexdigest()
	if myhash[0:5]=="00000":
		stoploop=True
	cnt+=1
	
print(mystring)
print(myhash)