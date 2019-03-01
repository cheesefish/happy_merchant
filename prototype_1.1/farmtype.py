#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from wareamount import WareAmount

#FarmType represents a type of farm. There is exactly one unique instance of every type of farm.
#The instances of FarmType are loaded from file and kept in a dictionary with name as key.
class FarmTypeABC(ABC):
	def __init__(self):
		self.key = str() #Name of farm type. Used as dictionary key. Exemple names: "Grains farm", "Cattle farm", "Wineyard".
		self.outputs = list([WareAmount()]) #Farms' production output.

################################################################################
#IMPLEMENTATION

class FarmType(FarmTypeABC):
	def __str__(self):
		return str(self.key)

################################################################################
#TEST CODE

import unittest

class TestFarmType(unittest.TestCase):
	def test_attributes(self):
		t = FarmType()
		t.key
		t.outputs[0]

if __name__ == "__main__":
	unittest.main(exit=False)