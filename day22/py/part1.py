import itertools
import sys
import math
import time
import collections
from random import sample

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()


def setinitial():#Function to define the initial conditions
    currentstate=dict()
    #currentstate["player"]={"hp":10,"armor":0,"mana":250} #example 1
    currentstate["player"]={"hp":50,"armor":0,"mana":500} #real one
    #currentstate["boss"]={"hp":13,"damage":8}
    #currentstate["boss"]={"hp":14,"damage":8} #example 2
    currentstate["boss"]={"hp":71,"damage":10} #real one
    currentstate["effects"]={"sheild":0,"poison":0,"recharge":0} #roundsleft
    currentstate["manaspent"]=0
    currentstate["result"]=""
    return(currentstate)


def applyplayereffects(currentstate):#function to apply player effects and decrease round
    if currentstate["effects"]["sheild"]>0:
        currentstate["effects"]["sheild"]-=1

    if currentstate["effects"]["sheild"]==0 and currentstate["player"]["armor"]>0:
        currentstate["player"]["armor"]=0
    
    if currentstate["effects"]["poison"]>0:
        currentstate["effects"]["poison"]-=1
        currentstate["boss"]["hp"]-=3

    if currentstate["effects"]["recharge"]>0:
        currentstate["effects"]["recharge"]-=1
        currentstate["player"]["mana"]+=101

    return(currentstate)


def battle(currentstate,move):#Function to perform the battle given a current state and single move

    currentstate=applyplayereffects(currentstate) ## Apply player effects
    if currentstate["boss"]["hp"]<=0:
        currentstate["result"]="Boss Died"

    ## Players turn
    elif move=="magic missle":
        currentstate["player"]["mana"]-=53
        currentstate["manaspent"]+=53
        currentstate["boss"]["hp"]-=4
    elif move=="drain":
            currentstate["player"]["mana"]-=73
            currentstate["manaspent"]+=73
            currentstate["boss"]["hp"]-=2
            currentstate["player"]["hp"]+=2
    elif move=="sheild" and currentstate["effects"]["sheild"]==0:
        currentstate["player"]["mana"]-=113
        currentstate["manaspent"]+=113
        currentstate["effects"]["sheild"] = 6
        currentstate["player"]["armor"]=7
    elif move=="poison" and currentstate["effects"]["poison"]==0:
        currentstate["player"]["mana"]-=173
        currentstate["manaspent"]+=173
        currentstate["effects"]["poison"] = 6
    elif move=="recharge" and currentstate["effects"]["recharge"]==0:
        currentstate["player"]["mana"]-=229
        currentstate["manaspent"]+=229
        currentstate["effects"]["recharge"] = 5 
    else:
        currentstate["result"]="Effect Already On"

     #end of player turn   
    if currentstate["player"]["mana"]<0:
        currentstate["result"]="Mana Overspend"
    elif currentstate["result"]=="Effect Already On":
        pass
    elif currentstate["boss"]["hp"]<=0:
            currentstate["result"]="Boss Died"
    else:#Do the boss turn
        currentstate=applyplayereffects(currentstate) ## Apply player effects
        if currentstate["boss"]["hp"]<=0:
            currentstate["result"]="Boss Died"
        else:# Boss's turn
            currentstate["player"]["hp"]-=(currentstate["boss"]["damage"]-currentstate["player"]["armor"])
            if currentstate["player"]["hp"]<=0:
                currentstate["result"]="Player Died"

    return(currentstate)

###
# Loop to check and build move combos
###

moveset = collections.deque([["magic missle"],["drain"],["sheild"],["poison"],["recharge"]])
# moveset = collections.deque([["sheild","recharge","poison"]])

rnd=0 #round number, ie number of moves in combo
resultdict=dict() #dictionary to store results
while True:
    if len(moveset)==0:#stop the loop if there's no moves
        break
    rnd+=1
    newmoveset=collections.deque()
    
    print("The round:",rnd, "Number of sequences:",len(moveset),"Time Elapsed:",round(time.time()-startsec,5))
    print("Time:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    print("Sample moveset:",sample(moveset,1))
    printit=True
    for cnt,thesequence in enumerate(moveset):#iterate over each sequence in movespace
        thestatus=setinitial() #set initial state for this sequence
        i=0 #move counter
        for themove in thesequence:  #iterate over each move in a given sequence       
            if thestatus["result"] =="":#If result not determined continue battle
                thestatus=battle(currentstate=thestatus,move=themove)
            if thestatus["result"] =="Boss Died":
                resultdict[tuple(thesequence)[:-1]]=thestatus["manaspent"]
                break
            elif thestatus["result"] !="": #stop if result determined, ie player dies, mana overspend, effect already on
                break
            # if i+1==rnd and thestatus["result"] == "" and thestatus["boss"]["hp"]-thestatus["player"]["hp"]<35:
            if i+1==rnd and thestatus["result"] == "" and thestatus["manaspent"]<=1937:
                #else if we have done the last move in the moveset and haven't come to a result then
                #then append each spell to the end and try these moves next round
                #i+1==rnd here makes it so this condition is only evaluated after the last move
                if printit==True:
                    print("Post first complete battle:",thestatus)
                    printit=False

                temp = thesequence.copy()
                temp.append("magic missle")
                newmoveset.append(temp)

                temp = thesequence.copy()
                temp.append("drain")
                newmoveset.append(temp)

                temp = thesequence.copy()
                temp.append("sheild")
                newmoveset.append(temp)

                temp = thesequence.copy()
                temp.append("poison")
                newmoveset.append(temp)

                temp = thesequence.copy()
                temp.append("recharge")
                newmoveset.append(temp)
                
            i+=1

    moveset=newmoveset.copy()

    if len(resultdict.keys())>0:
        minmana = min(resultdict.values())
        print("Lowest Mana to Win:",min(resultdict.values()))
        print("Total Winning Games:",len(resultdict.keys()))
        print("A sequences with min values:")
        print(sample([key for key in resultdict.keys() if resultdict[key]==minmana],1))
    print("\n")

if len(resultdict.keys())>0:
    print("Final Lowest Mana to Win:",min(resultdict.values()))
    print("Final Total Winning Games:",len(resultdict.keys()))
    print(resultdict.values())
else:
    print("No Results!")
print("Start:",start,"End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Total Time Elapsed:",round(time.time()-startsec,5))


