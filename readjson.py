#!/usr/bin/python

# prints the names of all settlements and their wares

# Imports
import json
    
with open('world.json', 'r') as w:
	world_dict = json.load(w)
	
for contents in world_dict:
	for settlements in (contents['settlements']):
		print(settlements['name'])
		for wares in (settlements['wares']):
			print("\t" + wares['name'])
