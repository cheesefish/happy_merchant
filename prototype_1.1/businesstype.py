################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from wareamount import WareAmount
from workertype import WorkerType

#BusinessType represents a type of business. There is exactly one unique instance of every type of business.
#The instances of BusinessType are loaded from file and kept in a dictionary with name as key.
class BusinessTypeABC(ABC):
	def __init__(self):
		self.key = str() #Name of business type. Used as dictionary key. Example names: "Bakery", "Brewery", "Blacksmith".
		self.inputs = list([WareAmount()]) #Business' production input resources.
		self.outputs = list([WareAmount()]) #Business' production output.
		self.staffTypes = list([WorkerType()]) #List of workers produced by this business

################################################################################
#IMPLEMENTATION

class BusinessType(BusinessTypeABC):
	def __str__(self):
		return str(self.key)

################################################################################
#TEST CODE

import unittest

class TestBusinessType(unittest.TestCase):
	def test_attributes(self):
		t = BusinessType()
		t.key
		t.inputs[0]
		t.outputs[0]
		t.staffTypes[0]

if __name__ == "__main__":
	unittest.main(exit=False)