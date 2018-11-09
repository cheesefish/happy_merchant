#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from waretype import WareTypeABC

#A certain amount of a given ware. Usually doesn't represent 'real' goods. Rather represents e.g. input, output, or needs.
class WareAmountABC(ABC):
	def __init__(self):	
		self.wareType = WareTypeABC()
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
	def weight(self):
		pass
	def transferTo(self, other, amount):
		pass
	def transferFrom(self, other, amount):
		pass

################################################################################
#TEST CODE

import unittest

class TestWareAmount(unittest.TestCase):
	def test_attributes(self):
		t = WareAmount()
		t.wareType
		t.amount
	def weight(self):
		pass
	def transferTo(self):
		pass
	def transferFrom(self):
		pass

if __name__ == "__main__":
	unittest.main(exit=False)