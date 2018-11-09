from abc import ABC, abstractmethod
from wareamount import WareAmount

################################################################################
#ABSTRACT CODE

#FarmType represents a type of farm. There is exactly one unique instance of every type of farm.
#The instances of FarmType are loaded from file and kept in a dictionary with name as key.
class FarmTypeABC(ABC):
	def __init__(self):
		self.key = str() #Name of farm type. Used as dictionary key. Exemple names: "Grains farm", "Cattle farm", "Wineyard".
		self.outputs = list() #Farms' production output.

################################################################################
#IMPLEMENTATION

class FarmType(FarmTypeABC):
	def __str__(self):
		return str(self.key)

################################################################################
#TEST CODE

if __name__ == "__main__":
	FarmType()
