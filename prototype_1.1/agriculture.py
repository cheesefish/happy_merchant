#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from farmtype import FarmType

#Represents the agricultural production of a town.
class AgricultureABC(ABC):
	def __init__(self):
		self.acres = int() #arable land available to town in acres
		self.farmtypes = list([FarmType()]) #types of wares farmed on town's arable land
		self.percent = list([float()]) #% of each ware type farmed out of arable land

################################################################################
#IMPLEMENTATION

class Agriculture(AgricultureABC):
	pass

################################################################################
#TEST CODE

import unittest

class TestWorker(unittest.TestCase):
	def test_attributes(self):
		t = Agriculture()
		t.acres
		t.farmtypes[0]
		t.percent[0]

if __name__ == "__main__":
	unittest.main(exit=False)