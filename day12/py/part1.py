import sys
import re

#Read data 
text_file = open("../input.txt", "r")
lines = text_file.readlines()[0]

mylist=[int(x) for x in re.findall(r'-?\d+', lines)]
print("Final Answer:",sum(mylist))