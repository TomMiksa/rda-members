class Group:
	def __init__(self, name, ids):
		self.name = name
		self.ids = ids
	
def loadFromFile(filename):
	f = open(filename)
	lines = f.readlines()
	f.close()
	return lines


def createDataStructures(lines):
	group_list = []
	group_name = ""
	group_ids = []
	first_header = True

	for line in lines:
	
		#remove rubbish from the file, e.g. remove &amp; #2 from Data Type Registries WG
		line = line.split("WG")[0]
		
		#if starts with = then read  next line
		if "=" in line :
			continue
		
		#if doesn't contain ; -> group  name 
		if ";" not in line :
			if first_header == True :
				group_name = line
				first_header = False
				continue
			else :
				group_list.append(Group(group_name, group_ids))
				group_ids = []
				group_name = line
		else :	
			# add the member to the list
			group_ids.append(line.split(';')[0])
	
	#append last group
	group_list.append(Group(group_name, group_ids))
	return group_list
	

def displayGroupsWithIds(group_list):
	for group in group_list :
		print ("Name " + group.name)
		for id in group.ids :
			print ("ID " + id)

def computeStats(group_list) :
	stats = {}

	# to compare groups once only, used for slicing
	x = 0
	for groupA in group_list :
		x += 1
		for groupB in group_list[x:] :
			counter = 0
			if groupA.name == groupB.name :
				continue
			
			for idA in groupA.ids :
				#print ("id: ", idA, "counter value: ", counter)
				for idB in groupB.ids :
					if idA == idB :
						counter += 1
						#if found, no need to iterate further
						break;
			
			stats[(groupA.name, groupB.name)] = counter	
	
	return stats

############ MAIN

import sys

if len(sys.argv) < 2 :
	print ("Provide path to a file with a list of groups, e.g. result-WGs.txt")
	sys.exit(-1)

filename = sys.argv[1] 
	
# Load the list of groups into lines variable
lines = loadFromFile('result-WGs.txt')

# Parse the list
group_list = createDataStructures(lines)

# compute statistics
stats = computeStats(group_list)	

# display stats
stats_view = [ (v,k) for k,v in stats.items() ]
stats_view.sort(reverse=True) 
for v,k in stats_view:
    print (v, k)