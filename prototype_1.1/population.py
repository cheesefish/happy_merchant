from abc import ABC, abstractmethod
from household import Household

################################################################################
#ABSTRACTION

#Represents the population of a town, consisting of multiple households.
class PopulationABC(ABC):
	def __init__(self):
		self.households = list()

	#Returns sum of household sizes, i.e. total population size.
	@abstractmethod
	def size(self): pass

################################################################################
#IMPLEMENTATION

class Population(PopulationABC):
	pass

################################################################################
#TEST CODE

if __name__ == "__main__":
	Population()
