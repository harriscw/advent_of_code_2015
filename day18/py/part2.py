import sys
from itertools import product, starmap, islice

#Read data 
text_file = open("../input.txt", "r")
grid =[list(v.strip("\n")) for v in text_file.readlines()]

def findNeighbors(grid, x, y): #stolen verbatim: https://stackoverflow.com/questions/16245407/python-finding-neighbors-in-a-2-d-list
    xi = (0, -1, 1) if 0 < x < len(grid) - 1 else ((0, -1) if x > 0 else (0, 1))
    yi = (0, -1, 1) if 0 < y < len(grid[0]) - 1 else ((0, -1) if y > 0 else (0, 1))
    return list(islice(starmap((lambda a, b: grid[x + a][y + b]), product(xi, yi)), 1, None))

#set the corners to be initially on
grid[0][0]="#"
grid[0][len(grid)-1]="#"
grid[len(grid)-1][0]="#"
grid[len(grid)-1][len(grid)-1]="#"

step=0
newgrid = grid
while step<100: #do 100 steps
    thisgrid=newgrid #define the current grid we'll iterate over
    print("Step:",step)
    #for row in thisgrid:
    #    print(row)
    
    turnoff=[]
    turnon=[]
    for i,row in enumerate(thisgrid): #iterate over each point in the grid
        for j,col in enumerate(thisgrid[i]):
            #print(i,j,"the point",thisgrid[i][j],"neighbors",findNeighbors(thisgrid, i, j))
            neighborcnt=findNeighbors(thisgrid, i, j).count("#") #count all the on lights for a given point
            if thisgrid[i][j]=="#" and neighborcnt not in [2,3] and (i,j) not in [(0,0),(0,len(thisgrid)-1),(len(thisgrid)-1,0),(len(thisgrid)-1,len(thisgrid)-1)]: #if it meets turn off criteria append it to a list
                turnoff.append((i,j))
            elif neighborcnt == 3: #if it meets turn on criteria append it to a list
                turnon.append((i,j))
    for j in turnoff: #now turn applicable lights off
        newgrid[j[0]][j[1]]="."
    for k in turnon: #and turn applicable lights on
        newgrid[k[0]][k[1]]="#"
    step+=1
    
print("Final Answer:",sum([x.count("#") for x in newgrid]))#sum all the on lights