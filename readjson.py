#!/usr/bin/python

# prints the names of all settlements in the world

# Imports
import json
    
with open('world.json', 'r') as w:
	world_dict = json.load(w)
	
for contents in world_dict:
	for settlement in (contents['settlement']):
		print(settlement['name'])
