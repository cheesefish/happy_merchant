#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from warebatch import WareBatch

#Represents a collection of ware batches, an inventory; e.g. market, business, or personal inventory. 
class WareStockABC(ABC):
	def __init__(self):	
		self.batches = dict(zip([str()], [WareBatch()]))

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
	def updatePerishabilities(self):
		pass
	def resetPerishabilities(self):
		pass
	def mergeBatches(self):
		pass

################################################################################
#TEST CODE

import unittest

class TestWareStock(unittest.TestCase):
	def test_attributes(self):
		t = WareStock()
		t.batches[str()]
	def test_updatePerishabilities(self):
		pass
	def test_resetPerishabilities(self):
		pass
	def test_mergeBatches(self):
		pass

if __name__ == "__main__":
	unittest.main(exit=False)
