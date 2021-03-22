import sys
from functools import reduce
import time

startsec = time.time()
#thenum=9
thenum=34000000

#I tried this but it was slow:
#https://www.programiz.com/python-programming/examples/factor-number
# I also tried starting at later houses like house 1000000 and searching from there
# I also started searching by every 10 houses feeling like that had more factors than numbers ending in 7, 3, etc
#ultimately I looked for a more efficient way to find factors.  I explored deque but found this and it was super fast:

def get_factors(n):  #https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    return sum(set(reduce(list.__add__, 
                ([10*i, 10*n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
# print(get_factors(8))

house=0
while True:
    house+=10
    housesum=get_factors(house)
    #print(house,housesum)
    if housesum>thenum:
        break
    # if house % 1000==0:
    #     print(house,housesum)

print("Run Time:",round(time.time()-startsec,5)) #takes about 2min for every house, 13s for every 10 house
print("Final Answer:",house,housesum)