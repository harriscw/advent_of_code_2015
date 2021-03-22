import sys
from functools import reduce
import time

startsec = time.time()
thenum=34000000

# The difference here vs part 1 is that I found if elves only go to 50 houses then you can filter out 
# factors where 50 times the factor is less than the number youre getting the factors of.
# That sentence is pretty confusing, lets do an example:
# Lets say elves only go to 5 houses.  And lets count presents for house 12.  The factors for 12 are:
# 1,2,3,4,6,12
# 1 represents the elf going to all houses.  This elf stops after 5 houses (1*5) so they dont make it to 12.
# 2 represents the elf going to every other house.  This elf stops at 10 (2*5) so they dont make it to 12.
# 3 represents the elf going to every third house.  This elf makes it to 12 on their 4th house.
# So by this pattern if a factor * 5 < 12 you don't count it.
# Then for this problem for a given number if a factor*50 is < the given number then filter it out.

def get_factors(n):  #https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    return sum(set(reduce(list.__add__, 
                ([11*x for x in [i, n//i] if 50*x>=n] for i in range(1, int(n**0.5) + 1) if n % i == 0) 
                )))

# print(get_factors(12))
# sys.exit()
house=786240 #I figure its gotta be more than the answer for part 1 since we're losing factors, right?
seen=False
while seen==False:
    house+=10
    housesum=get_factors(house)
    if housesum>thenum:
        seen=True
    if house % 1000==0:
        print(house,housesum)

print("Run Time:",round(time.time()-startsec,5)) #1s (with print on) starting at p1 answer every 10 houses, 11s every house
print("Final Answer:",house,housesum) #18s (with print on) starting from 0 every 10 houses, 148s every house