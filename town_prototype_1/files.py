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
	wares = data['wares']
	for ware in wares:
		name = ware['name']
		WARES[str(Ware(name))] = Ware(name)
	

def loadAgriculturesTemp():
	k = 0.001	
	agricultures = data['agricultures']	
	for agriculture in agricultures:
		farm = agriculture['type']
		farm_products = []
		output_wares = agriculture['output']
		for ware in output_wares:
			farm_products.append(ProductionIO(ware['ware'],k*ware['amount']))
		AGRICULTURES[str(Agriculture(farm, farm_products))] = Agriculture(farm, farm_products)	 
		
def loadIndustriesTemp():
	industries = data['industries']
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
	settlements = data['settlements']
	for settlement in settlements:
		name = settlement['name']
		population = settlement['population']
		acres = settlement['acres']
		town = Town(name, acres)
		
		land_allocation = []
		lands = settlement['land allocation']
		for land in lands:
			land_allocation.append(AgricultureAllocation(AGRICULTURES[land['type']], land['acres']))
		town.agriallocs = land_allocation
		
		businesses = settlement['Businesses']
		for business in businesses:
			town.addBusiness(Business(business['name'],INDUSTRIES[str(business['type'])]))
		TOWNS[settlement['name']] = town
	
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
