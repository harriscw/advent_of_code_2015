import itertools
import sys
import math
import time

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()


def setinitial():
    #Define the initial conditions
    currentstate=dict()
    #currentstate["player"]={"hp":10,"armor":0,"mana":250} #example 1
    currentstate["player"]={"hp":50,"armor":0,"mana":500} #real one
    # currentstate["boss"]={"hp":13,"damage":8}
    #currentstate["boss"]={"hp":14,"damage":8} #example 2
    currentstate["boss"]={"hp":71,"damage":10} #real one
    currentstate["effects"]={"sheild":0,"poison":0,"recharge":0} #roundsleft
    currentstate["manaspent"]=0
    currentstate["result"]=""
    return(currentstate)


def applyplayereffects(currentstate):
    if currentstate["effects"]["sheild"]>0:
        currentstate["effects"]["sheild"]-=1
    else:
        currentstate["player"]["armor"]==0
    
    if currentstate["effects"]["poison"]>0:
        currentstate["effects"]["poison"]-=1
        currentstate["boss"]["hp"]-=3

    if currentstate["effects"]["recharge"]>0:
        currentstate["effects"]["recharge"]-=1
        currentstate["player"]["mana"]+=101
    return(currentstate)


def battle(currentstate,move):

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
    else:
        currentstate=applyplayereffects(currentstate) ## Apply player effects
        if currentstate["boss"]["hp"]<=0:
            currentstate["result"]="Boss Died"
        else:# Boss's turn
            currentstate["player"]["hp"]-=(currentstate["boss"]["damage"]-currentstate["player"]["armor"])
        if currentstate["player"]["hp"]<=0:
            currentstate["result"]="Player Died"

    return(currentstate)

themoves = ["magic missle","drain","sheild","poison","recharge"]
dont4=[('magic missle', 'magic missle', 'poison', 'recharge'), ('magic missle', 'drain', 'poison', 'recharge'), ('magic missle', 'sheild', 'poison', 'recharge'), ('magic missle', 'poison', 'magic missle', 'recharge'), ('magic missle', 'poison', 'drain', 'recharge'), ('magic missle', 'poison', 'sheild', 'recharge'), ('drain', 'magic missle', 'poison', 'recharge'), ('drain', 'drain', 'poison', 'recharge'), ('drain', 'sheild', 'poison', 'recharge'), ('drain', 'poison', 'magic missle', 'recharge'), ('drain', 'poison', 'drain', 'recharge'), ('drain', 'poison', 'sheild', 'recharge'), ('sheild', 'magic missle', 'poison', 'recharge'), ('sheild', 'drain', 'poison', 'recharge'), ('sheild', 'poison', 'magic missle', 'recharge'), ('sheild', 'poison', 'drain', 'recharge'), ('sheild', 'poison', 'recharge', 'magic missle'), ('sheild', 'poison', 'recharge', 'drain'), ('sheild', 'poison', 'recharge', 'sheild'), ('poison', 'magic missle', 'magic missle', 'recharge'), ('poison', 'magic missle', 'drain', 'recharge'), ('poison', 'magic missle', 'sheild', 'poison'), ('poison', 'magic missle', 'sheild', 'recharge'), ('poison', 'drain', 'magic missle', 'recharge'), ('poison', 'drain', 'drain', 'recharge'), ('poison', 'drain', 'sheild', 'poison'), ('poison', 'drain', 'sheild', 'recharge'), ('poison', 'sheild', 'magic missle', 'poison'), ('poison', 'sheild', 'magic missle', 'recharge'), ('poison', 'sheild', 'drain', 'poison'), ('poison', 'sheild', 'drain', 'recharge'), ('poison', 'sheild', 'recharge', 'magic missle'), ('poison', 'sheild', 'recharge', 'drain'), ('poison', 'sheild', 'recharge', 'poison')]

def runsequences(nummoves,printnum):
    #create generator for all move combos of a certain length. 
    #Originally had it as a list but when I got to 12 it crashed my computer just trying to make the list
    maxeffects=math.ceil(nummoves/3) #this is the max number of a single given effect you can have in a moveset

    #moveset = [["recharge","sheild","drain","poison","magic missle"]]
    moveset = itertools.product(themoves, repeat=nummoves)
    #remove consecutives. filter false is like "remove when true"
    moveset = itertools.filterfalse(lambda themove: [k for k,g in itertools.groupby(themove)].count("recharge")<themove.count("recharge"),moveset) 
    moveset = itertools.filterfalse(lambda themove: [k for k,g in itertools.groupby(themove)].count("sheild")<themove.count("sheild"),moveset) 
    moveset = itertools.filterfalse(lambda themove: [k for k,g in itertools.groupby(themove)].count("poison")<themove.count("poison"),moveset) 
    #remove >max
    moveset=itertools.filterfalse(lambda themove: (themove.count("sheild")>maxeffects) or (themove.count("poison")>maxeffects) or (themove.count("recharge")>maxeffects) or themove[0:2].count("recharge")==2 or themove[0:2].count("sheild")==2 or themove[0:2].count("recharge")==2,moveset)    
    # your count is exactly the max number you can have but spell isn't the first and last in the sequence   
    moveset=itertools.filterfalse(lambda themove: themove.count("recharge")>=maxeffects and not(themove[0]=="recharge" and themove[-1]=="recharge"),moveset) 
    moveset=itertools.filterfalse(lambda themove: themove.count("sheild")>=maxeffects and not(themove[0]=="sheild" and themove[-1]=="sheild"),moveset) 
    moveset=itertools.filterfalse(lambda themove: themove.count("poison")>=maxeffects and not(themove[0]=="poison" and themove[-1]=="poison"),moveset)
    # dont start - way too slow
    # moveset=itertools.filterfalse(lambda themove: themove[0:4] in dont4,moveset)
    moveset=itertools.filterfalse(lambda themove: themove[0] =="magic missle",moveset)

    resultdict=dict()
    for cnt,thesequence in enumerate(moveset):#iterate over move space
        if cnt % printnum==0:
            print("Move number",cnt)
        #print("Sequence",thesequence)
        thestatus=setinitial() #set initial state
        for themove in thesequence:  
            #print(i)            
            if thestatus["result"] =="":#If result not determined continue battle
                thestatus=battle(currentstate=thestatus,move=themove)
            elif thestatus["result"] =="Boss Died":
                resultdict[thesequence]={"result":thestatus["result"],"manaspent":thestatus["manaspent"]}
                break
            else: #stop if result determined, ie player dies, boss dies, mana overspend, effect already on
                break
            #print(thestatus)
            if thestatus["result"] != "":#stop if result determined, ie player dies, boss dies, mana overspend, effect already on
                #print("has result",thesequence,thestatus["result"])
                dont4.append(thesequence)
                break

    # print(dont4)
    print("Final number of moves:",cnt+1,"/",len(themoves)**nummoves)

    return(resultdict)

#print(runsequences(nummoves=4,printnum=1000000))
#print(runsequences(nummoves=7,printnum=10000))
print(runsequences(nummoves=10,printnum=1000000)) #9765625, 328s -> 8984375, 177s -> 3126556 166s
#print(runsequences(nummoves=11,printnum=1000000)) #48828125, 951s ie 15min -> (11s with no function)
#print(runsequences(nummoves=12,printnum=1000000)) #244140625, 4494s ie 75 min ie 1.25 hrs ->
#print(runsequences(nummoves=13,printnum=1000000)) #1123046875 / 1220703125, 9 hrs

# nummoves=5
# moveset = itertools.product(themoves, repeat=nummoves)
# maxeffects=math.floor(nummoves/3)
# themoves = ["magic missle","drain","sheild","poison","recharge"]
# moveset = itertools.product(themoves, repeat=nummoves)
#this is ugly.  But it finds positions of all occurences of a spell (e.g. "sheild") and then finds the difference with the nearest neighbor.  If any <3 it filters.
# moveset = itertools.filterfalse(lambda themove:any(ele <3 for ele in [[i for i, x in enumerate(themove) if x == "sheild"][n]-[i for i, x in enumerate(themove) if x == "sheild"][n-1] for n in range(1,len([i for i, x in enumerate(themove) if x == "sheild"]))]),moveset)
# moveset = itertools.filterfalse(lambda themove:any(ele <3 for ele in [[i for i, x in enumerate(themove) if x == "poison"][n]-[i for i, x in enumerate(themove) if x == "poison"][n-1] for n in range(1,len([i for i, x in enumerate(themove) if x == "poison"]))]),moveset)
# moveset = itertools.filterfalse(lambda themove:any(ele <3 for ele in [[i for i, x in enumerate(themove) if x == "recharge"][n]-[i for i, x in enumerate(themove) if x == "recharge"][n-1] for n in range(1,len([i for i, x in enumerate(themove) if x == "recharge"]))]),moveset)

# moveset = itertools.filterfalse(lambda themove:[[i for i, x in enumerate(themove) if x == "sheild"][n]-[i for i, x in enumerate(themove) if x == "sheild"][n-1] for n in range(1,len([i for i, x in enumerate(themove) if x == "sheild"]))],moveset)


# #remove consecutives.  filter false is like remove when true
# moveset = itertools.filterfalse(lambda themove: [k for k,g in itertools.groupby(themove)].count("recharge")<themove.count("recharge"),moveset) 
# moveset = itertools.filterfalse(lambda themove: [k for k,g in itertools.groupby(themove)].count("sheild")<themove.count("sheild"),moveset) 
# moveset = itertools.filterfalse(lambda themove: [k for k,g in itertools.groupby(themove)].count("poison")<themove.count("poison"),moveset) 
# #remove >max
# moveset=itertools.filterfalse(lambda themove: (themove.count("sheild")>maxeffects) or (themove.count("poison")>maxeffects) or (themove.count("recharge")>maxeffects) or themove[0:2].count("recharge")==2 or themove[0:2].count("sheild")==2 or themove[0:2].count("recharge")==2,moveset)    
# # your count is exactly the max number you can have but spell isn't the first and last in the sequence   
# moveset=itertools.filterfalse(lambda themove: themove.count("recharge")==nummoves/3 and not (themove[0]=="recharge" and themove[-1]=="recharge"),moveset)
# moveset=itertools.filterfalse(lambda themove: themove.count("sheild")==nummoves/3 and not (themove[0]=="sheild" and themove[-1]=="sheild"),moveset) 
# moveset=itertools.filterfalse(lambda themove: themove.count("poison")==nummoves/3 and not (themove[0]=="poison" and themove[-1]=="poison"),moveset)


#this is ugly.  But it finds positions of all occurences of a spell (e.g. "sheild") and then finds the difference with the nearest neighbor.  If any <3 it filters.
#its much slower
# moveset = itertools.filterfalse(lambda themove: any(ele <3 for ele in np.diff([i for i, x in enumerate(themove) if x == "sheild"])),moveset)
# moveset = itertools.filterfalse(lambda themove: any(ele <3 for ele in np.diff([i for i, x in enumerate(themove) if x == "poison"])),moveset)
# moveset = itertools.filterfalse(lambda themove: any(ele <3 for ele in np.diff([i for i, x in enumerate(themove) if x == "recharge"])),moveset)


# for cnt,move in enumerate(moveset):
#     print(cnt+1,move,move[0:4])

print("Start:",start,"End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))



