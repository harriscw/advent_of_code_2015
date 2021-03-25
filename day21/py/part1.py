import sys
from operator import add

text_file = open("../attributes.txt", "r")
mylist =[list(filter(None,v.strip("\n").split("  "))) for v in text_file.readlines()]

mydict=dict() #0 = cost, 1 = damage, 2 = armor
for sublist in mylist:
    #print(sublist)
    if len(sublist)>0 and ":" not in sublist[0]:
        mydict[sublist[0]]=[int(sublist[1]),int(sublist[2]),int(sublist[3])]

weapons=["Dagger","Shortsword","Warhammer","Longsword","Greataxe" ]
armor=['Leather', 'Chainmail', 'Splintmail', 'Bandedmail', 'Platemail']
rings=['Damage +1','Damage +2','Damage +3','Defense +1','Defense +2','Defense +3']

def battle(player=[8,5,5],boss=[12,7,2]):
    player_hp=player[0]
    boss_hp=boss[0]
    round=0
    #print(round,"Boss HP:",boss_hp,"Player HP:",player_hp)
    while True:
        round+=1
        boss_hp-=max(player[1]-boss[-1],1)#0 = HP, 1 = damage, 2 = armor
        if boss_hp<=0:
            print(round,"Boss HP:",boss_hp,"Player HP:",player_hp)
            return("Player")
        player_hp-=max(boss[1]-player[-1],1)#0 = HP, 1 = damage, 2 = armor
        if player_hp<=0:
            print(round,"Boss HP:",boss_hp,"Player HP:",player_hp)
            return("Boss")
        #print(round,"Boss HP:",boss_hp,"Player HP:",player_hp)
        
#print(battle())

costdict=dict()
allcombos = list()

# Must have one weapon, armor, rings are optional

for thisweapon in weapons: #weapon
    allcombos.append([thisweapon])

for thisweapon in weapons: #weapon, armor
    for thisarmor in armor:
        allcombos.append([thisweapon,thisarmor])

for thisweapon in weapons: #weapon, ring
    for thisring in rings:
        allcombos.append([thisweapon,thisring])

for thisweapon in weapons: #weapon, ring, ring
    for thisring1 in rings:
        for thisring2 in rings:
            if thisring1 != thisring2:
                allcombos.append([thisweapon,thisring1,thisring2])

for thisweapon in weapons: #weapon, armor, ring
    for thisarmor in armor:
        for thisring in rings:
            allcombos.append([thisweapon,thisarmor,thisring])

for thisweapon in weapons: #weapon, armor, ring, ring
    for thisarmor in armor:
        for thisring1 in rings:
            for thisring2 in rings:
                if thisring1 != thisring2:
                    allcombos.append([thisweapon,thisarmor,thisring1,thisring2])

# print(allcombos)
for combo in allcombos:
    print(combo)
    thissum=[0,0,0]
    for item in combo:
        thissum=list(map(add, thissum, mydict[item]))
        print(item,mydict[item])
    if(battle(player=[100,thissum[1],thissum[2]],boss=[103,9,2])=="Player"):
        costdict[tuple(combo)]=thissum[0]
    print(thissum)

print(costdict)
print("Final Answer:",list(costdict.keys())[list(costdict.values()).index(min(costdict.values()))],min(costdict.values()))