from abc import ABC, abstractmethod
from warebatch import WareBatch

################################################################################
#ABSTRACTION

#Represents a collection of ware batches, an inventory; e.g. market, business, or personal inventory. 
class WareStockABC(ABC):
	def __init__(self):	
		self.batches = dict()

	#Updates all batches' perishability stats.
	@abstractmethod
	def updatePerishabilities(self): pass

	#Resets perish stats of all batches to their full states.
	#Used by some stocks (e.g. markets) that doesn't deal with perishability.
	@abstractmethod
	def resetPerishabilities(self): pass

	#Merges all batches of same type.
	@abstractmethod
	def mergeBatches(self): pass

################################################################################
#IMPLEMENTATION

class WareStock(WareStockABC):
	pass

################################################################################
#TEST CODE

if __name__ == "__main__":
	WareStock()
