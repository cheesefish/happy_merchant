from abc import ABC, abstractmethod
from waretype import WareType

################################################################################
#ABSTRACTION

#A certain amount of a given ware. Usually doesn't represent 'real' goods. Rather represents e.g. input, output, or needs.
class WareAmountABC(ABC):
	def __init__(self):	
		self.wareType = WareType()
		self.amount = int()

	#Returns total weight (amount * waretype weight).
	@abstractmethod
	def weight(self): pass

	#Transfers amount to other WareAmount from self.
	@abstractmethod
	def transferTo(self, other, amount): pass

	#Transfers amount from other WareAmount to self.
	@abstractmethod
	def transferFrom(self, other, amount): pass

################################################################################
#IMPLEMENTATION

class WareAmount(WareAmountABC):
	pass

################################################################################
#TEST CODE

if __name__ == "__main__":
	WareAmount()