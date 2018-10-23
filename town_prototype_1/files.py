######################################
# Contains all data read from files. #
######################################

import json

from ware import Ware
from production import ProductionIO
from production import Industry
from production import Agriculture
from town import Town
from town import AgricultureAllocation
from business import Business

#######################################################
#FILE DATA

WARES = {} #dict of all loaded wares
AGRICULTURES = {} #dict of all loaded agricultures
INDUSTRIES = {} #dict of all loaded industries
TOWNS = {} #dict of all loaded towns

#json data
with open('data.json', 'r') as d:
		data = json.load(d)

#######################################################
#READ FUNCTIONS

def loadWaresTemp():
	wares = data[1]['wares']
	for ware in wares:
		name = ware['name']
		WARES[str(Ware(name))] = Ware(name)
	

def loadAgriculturesTemp():
	k = 0.001	
	agricultures = data[2]['agricultures']	
	for agriculture in agricultures:
		farm = agriculture['type']
		farm_products = []
		output_wares = agriculture['output']
		for ware in output_wares:
			farm_products.append(ProductionIO(ware['ware'],k*ware['amount']))
		AGRICULTURES[str(Agriculture(farm, farm_products))] = Agriculture(farm, farm_products)	 
		
def loadIndustriesTemp():
	industries = data[3]['industries']
	for industry in industries:
		artisan = industry['type']
		inputs = []
		input_wares = industry['input']
		for ware in input_wares:
			inputs.append(ProductionIO(ware['ware'], ware['amount']))
		outputs = []
		output_wares = industry['output']
		for ware in output_wares:
			outputs.append(ProductionIO(ware['ware'], ware['amount']))
		throughput = industry['throughput']
		INDUSTRIES[str(Industry(artisan, inputs, outputs, throughput))] = Industry(artisan, inputs, outputs, throughput)


def loadTestTownTemp():
	first_town = data[0]['settlements'][0]
	name = first_town['name']
	acres = first_town['acres']
	town = Town(name, acres)
	agriallocs = [
			AgricultureAllocation(AGRICULTURES["apple farm"], 10),
			AgricultureAllocation(AGRICULTURES["grain farm"], 50),
			AgricultureAllocation(AGRICULTURES["hops farm"], 20),
			AgricultureAllocation(AGRICULTURES["cattle farm"], 20)
		]
	town.agriallocs = agriallocs
	businesses = [
			Business("Joe's Bakery", INDUSTRIES["bakery"]),
			Business("Bob's Bakery", INDUSTRIES["bakery"]),
			Business("Ye Olde Brewery", INDUSTRIES["brewery"]),
			Business("The Cheese & Butter Company", INDUSTRIES["dairy"])
		]
	for business in businesses:
		town.addBusiness(business)
	TOWNS[name] = town
	
#######################################################
#EXECUTION CODE
		
loadWaresTemp()
loadAgriculturesTemp()
loadIndustriesTemp()
loadTestTownTemp()

#######################################################
#TEST CODE

if __name__ == "__main__":
	tab = " "
	print("Wares:")
	for ware in WARES:
		print(tab + str(ware))
	print()
	print("Agricultures:")
	for agriculture in AGRICULTURES:
		print(tab + str(agriculture))
	print()
	print("Industries:")
	for industry in INDUSTRIES:
		print(tab + str(industry))
	print()
