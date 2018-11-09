from abc import ABC, abstractmethod
from warestock import WareStock
from worker import Worker

################################################################################
#ABSTRACTION

#Represents a population unit, with its own inventory and a main provider.
class HouseholdABC(WareStock, ABC):
	def __init__(self):
		self.worker = Worker() #Main provider of household.
		self.size = int() #Number of people in the household.

################################################################################
#IMPLEMENTATION

class Household(HouseholdABC):
	pass

################################################################################
#TEST CODE

if __name__ == "__main__":
	Household()
