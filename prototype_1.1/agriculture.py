from abc import ABC, abstractmethod
from farmtype import FarmType

################################################################################
#ABSTRACTION

#Represents the agricultural production of a town.
class AgricultureABC(ABC):
	def __init__(self):
		self.acres = int() #arable land available to town in acres
		self.farmtypes = list() #types of wares farmed on town's arable land
		self.percent = list() #% of each ware type farmed out of arable land

################################################################################
#IMPLEMENTATION

class Agriculture(AgricultureABC):
	pass

################################################################################
#TEST CODE

if __name__ == "__main__":
	Agriculture()