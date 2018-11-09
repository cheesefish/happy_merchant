from abc import ABC, abstractmethod
from wareamount import WareAmount

################################################################################
#ABSTRACTION

#BusinessType represents a type of business. There is exactly one unique instance of every type of business.
#The instances of BusinessType are loaded from file and kept in a dictionary with name as key.
class BusinessTypeABC(ABC):
	def __init__(self):
		self.key = str() #Name of business type. Used as dictionary key. Example names: "Bakery", "Brewery", "Blacksmith".
		self.inputs = list() #Business' production input resources.
		self.outputs = list() #Business' production output.
		self.staffTypes = list() #List of workers produced by this business

################################################################################
#IMPLEMENTATION

class BusinessType(BusinessTypeABC):
	def __str__(self):
		return str(self.key)

################################################################################
#TEST CODE

if __name__ == "__main__":
	BusinessType()
