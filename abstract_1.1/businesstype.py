from wareamount import WareAmount

#BusinessType represents a type of business. There is exactly one unique instance of every type of business.
#The instances of BusinessType are loaded from file and kept in a dictionary with name as key.
class BusinessType:
	key = str() #Name of business type. Used as dictionary key. Example names: "Bakery", "Brewery", "Blacksmith".
	inputs = list(WareAmount()) #Business' production input resources.
	outputs = list(WareAmount()) #Business' production output.
	staffTypes = list(WorkerType()) #List of workers produced by this business
