import sys
import networkx as nx

#Read data 
text_file = open("../input.txt", "r")
lines =[v.strip("\n") for v in text_file.readlines()]

G = nx.Graph() #create network graph
for i,line in enumerate(lines):
	weight=int(line.split(" = ")[-1])#edge weight
	origin=line.split(" = ")[0].split(" to ")[0]#edge origin
	dest=line.split(" = ")[0].split(" to ")[-1]#edge destination
	G.add_edge(origin, dest, weight=weight)

goodpaths=list()#get all simple (i.e. no repeats) paths that touch all nodes, i.e. simple paths where length = total number of nodes
for sourcenode in list(G.nodes):#iterate over all combos of source and target nodes
	for targetnode in list(G.nodes):
		if sourcenode!=targetnode:
			allpaths=list(nx.all_simple_paths(G, sourcenode, targetnode))#get all simple paths for this combo
			for thispath in allpaths:#for all the simple paths keep it if ittouches all nodes (ie length is total node size)
				if len(thispath)==len(list(G.nodes)):
					goodpaths.append(thispath)
			
print("Number of paths",len(goodpaths))

mylengths=list()#now get the cumulative weights for all paths.  I should have done this as a dict so I could also easily get path as well
for out in goodpaths:
	acc=0
	for i in range(1,len(out)):#iteratively get weights between each nodes in the path
		prev = out[i-1]
		node = out[i]
		acc += G[prev][node]["weight"]
	mylengths.append(acc)

print(min(mylengths))#part1
print(max(mylengths))#part2