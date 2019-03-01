#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from market import Market
from agriculture import Agriculture
from business import Business
from population import Population

class TownABC(ABC):
	def __init__(self):
		self.market = Market()
		self.agriculture = Agriculture()
		self.businesses = list([Business()])
		self.population = Population()

################################################################################
#IMPLEMENTATION

class Town(TownABC):
	pass

################################################################################
#TEST CODE

import unittest

class TestTown(unittest.TestCase):
	def test_attributes(self):
		t = Town()
		t.market
		t.agriculture
		t.businesses[0]
		t.population

if __name__ == "__main__":
	unittest.main(exit=False)
