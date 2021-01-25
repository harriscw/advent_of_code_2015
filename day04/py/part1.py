import hashlib

secretkey="ckczppom"
#secretkey="abcdef"
#secretkey="pqrstuv"

cnt=0
stoploop=False
while stoploop==False:
	cnt+=1
	mystring=secretkey+str(cnt)
	myhash=hashlib.md5(mystring.encode("utf")).hexdigest()
	if myhash[0:5]=="00000":
		stoploop=True

print(mystring)
print(myhash)
print("Final Answer:",cnt)