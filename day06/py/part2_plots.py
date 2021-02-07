
# coding: utf-8

# In[1]:


import os
print(os.getcwd())


# In[5]:


import numpy as np
import sys
import time
import matplotlib.pyplot as plt

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
print("Start:",start)
startsec = time.time()

#Read data 
text_file = open("input.txt", "r")
lines =[v.strip("\n") for v in text_file.readlines()]
#lines=["turn on 0,0 through 999,999"]
#lines=["toggle 0,0 through 999,0"]
#lines=["turn off 499,499 through 500,500"]
#print(lines)

instrux=[] #get a list of lists with semi parsed instructions
for line in lines:
	newlist=line.split(" ")
	if newlist[0]=="toggle":
		instruct="toggle"
		lowerrow=int(newlist[1].split(",")[0])
		lowercol=int(newlist[1].split(",")[1])
	else:
		instruct=newlist[1]
		lowerrow=int(newlist[2].split(",")[0])
		lowercol=int(newlist[2].split(",")[1])
	upperrow=int(newlist[-1].split(",")[0])
	uppercol=int(newlist[-1].split(",")[1])
	instrux.append([instruct,lowerrow,upperrow,lowercol,uppercol])

#print(instrux)

mygrid = np.zeros((1000,1000),dtype=int) #create a grid of lights turned off
cnt=0
for instruction in instrux: #execute the instructions
	fig = plt.figure(figsize=(10, 10))
	plt.imshow(np.flipud(mygrid))
	plt.savefig('stupidplots/'+str(cnt).zfill(4) +".png")
	if instruction[0]=="on":
		for row in range(instruction[1],instruction[2]+1): #switch on
			for col in range(instruction[3],instruction[4]+1):
				mygrid[row,col]+=1
	elif instruction[0]=="off":
		for row in range(instruction[1],instruction[2]+1): #switch off
			for col in range(instruction[3],instruction[4]+1):
				mygrid[row,col]=max(0,mygrid[row,col]-1)
	else:
		for row in range(instruction[1],instruction[2]+1): #toggle
			for col in range(instruction[3],instruction[4]+1):
				mygrid[row,col]+=2
	cnt+=1

print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))
print("Final Answer: ",mygrid.sum())	


# In[2]:


fig = plt.figure(figsize=(10, 10))
plt.imshow(np.flipud(mygrid))
plt.show()

