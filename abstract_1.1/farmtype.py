from wareamount import WareAmount

#FarmType represents a type of farm. There is exactly one unique instance of every type of farm.
#The instances of FarmType are loaded from file and kept in a dictionary with name as key.
class FarmType:
	key = str() #Name of farm type. Used as dictionary key. Exemple names: "Grains farm", "Cattle farm", "Wineyard".
	outputs = list(WareAmount()) #Farms' production output.
