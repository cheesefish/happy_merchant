#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from wareamount import WareAmount

#WareBatch represents an amount of wares with the same perishability state.
class WareBatchABC(WareAmount, ABC):
	def __init__(self):	
		super().__init__()
		self.perishStatus = float() #Starts at 1.0 (100%) and is degraded over time.
		self.perishTimeLeft = int() #Countdown to next status degradation.

	#Decrements time left. When when time left reaches 0: reset time left and degrade status by specified amount (found in WareType).
	#When quality reaches 0: batch should be destroyed by caller; Raises exception.
	@abstractmethod
	def updatePerishability(self): pass

	#Transfers amount to other batch from self. Sets perish stats of other to the lowest values between self and other.
	@abstractmethod
	def transferToBatch(self, other, amount): pass

	#Transfers amount from other batch to self. Sets perish stats of self to the lowest values between self and other.
	@abstractmethod
	def transferFromBatch(self, other, amount): pass

	#Returns dictionary key derived from waretype, perish status, and time passed.
	@abstractmethod
	def key(self): pass

################################################################################
#IMPLEMENTATION

class WareBatch(WareBatchABC):
	def updatePerishability(self):
		pass
	def transferToBatch(self, other, amount):
		pass
	def transferFromBatch(self, other, amount):
		pass
	def key(self):
		pass

################################################################################
#TEST CODE

import unittest

class TestWareBatch(unittest.TestCase):
	def test_attributes(self):
		t = WareBatch()
		t.perishStatus
		t.perishTimeLeft
	def test_updatePerishability(self):
		pass
	def test_transferToBatch(self):
		pass
	def test_transferFromBatch(self):
		pass
	def test_key(self):
		pass

if __name__ == "__main__":
	unittest.main(exit=False)
