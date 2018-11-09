from abc import ABC, abstractmethod
from market import Market
from agriculture import Agriculture
from businesses import Business
from population import Population

################################################################################
#ABSTRACTION

class TownABC(ABC):
	def __init__(self):
		self.market = Market()
		self.agriculture = Agriculture()
		self.businesses = list()
		self.population = Population()

	#User interface of town.
	@abstractmethod
	def ui(self): pass

################################################################################
#IMPLEMENTATION

class Town(TownABC):
	pass

################################################################################
#TEST CODE

if __name__ == "__main__":
	Town()