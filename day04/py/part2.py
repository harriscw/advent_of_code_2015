import hashlib
import time

startsec = time.time()

secretkey="ckczppom"
#secretkey="abcdef"
#secretkey="pqrstuv"

cnt=0
stoploop=False
while stoploop==False:
	cnt+=1
	mystring=secretkey+str(cnt) #iteratively generate new string
	myhash=hashlib.md5(mystring.encode("utf")).hexdigest() #get the md5 hash
	if myhash[0:6]=="000000":
		stoploop=True

print("Run Time:",round(time.time()-startsec,5))
print(mystring)
print(myhash)
print("Final Answer:",cnt)