#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod

#WareType represents a type of tradable goods. There is exactly one unique instance of every type of Ware.
#The instances of WareType are loaded from file and kept in a dictionary with name as key.
class WareTypeABC(ABC):
	def __init__(self):
		self.key = str() #Name of ware type. Used as dictionary key. Example names: "Bread", "Spices", "Weapons".
		self.weight = float() #physical weight of smallest unit of this ware
		self.perishStep = float() #e.g. 0.1
		self.perishTime = int() #number of ticks before quality degrades one step

################################################################################
#IMPLEMENTATION

class WareType(WareTypeABC):
	def __str__(self):
		return str(self.key)

################################################################################
#TEST CODE

import unittest

class TestWareType(unittest.TestCase):
	def test_attributes(self):
		t = WareType()
		t.key
		t.weight
		t.perishStep
		t.perishTime

if __name__ == "__main__":
	unittest.main(exit=False)
