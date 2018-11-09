from abc import ABC, abstractmethod
from market import Market
from agriculture import Agriculture
from businesses import Business
from population import Population

################################################################################
#ABSTRACT CODE

class TownABC(ABC):
	def __init__(self):
		self.market = MarketABC()
		self.agriculture = AgricultureABC()
		self.businesses = list()
		self.population = PopulationABC()

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