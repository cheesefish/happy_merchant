#!/usr/bin/python

# Imports
import json
    
with open('world.json', 'r') as w:
	world = json.load(w)
	
# prints the names of all settlements and their wares
for contents in world:
	for settlements in (contents['settlements']):
		print(settlements['name'])
		for wares in (settlements['wares']):
			print("\t" + wares['name'])
			
			
#prints the name of the first settlement		
print(world[0]['settlements'][0]['name'])

#print the name of the first ware in the first settlement
print(world[0]['settlements'][0]['wares'][0]['name'])
