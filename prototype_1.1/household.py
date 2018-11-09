#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from warestock import WareStock
from worker import Worker

#Represents a population unit, with its own inventory and a main provider.
class HouseholdABC(WareStock, ABC):
	def __init__(self):
		super().__init__()
		self.worker = Worker() #Main provider of household.
		self.size = int() #Number of people in the household.

################################################################################
#IMPLEMENTATION

class Household(HouseholdABC):
	pass

################################################################################
#TEST CODE

import unittest

class TestHousehold(unittest.TestCase):
	def test_attributes(self):
		t = Household()
		t.worker
		t.size

if __name__ == "__main__":
	unittest.main(exit=False)