#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from household import Household

#Represents the population of a town, consisting of multiple households.
class PopulationABC(ABC):
	def __init__(self):
		self.households = list([Household()])

	#Returns sum of household sizes, i.e. total population size.
	@abstractmethod
	def size(self): pass

################################################################################
#IMPLEMENTATION

class Population(PopulationABC):
	def size(self):
		pass

################################################################################
#TEST CODE

import unittest

class TestPopulation(unittest.TestCase):
	def test_attributes(self):
		t = Population()
		t.households[0]
	def test_size(self):
		pass

if __name__ == "__main__":
	unittest.main(exit=False)
