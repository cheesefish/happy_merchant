#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from warestock import WareStock
from businesstype import BusinessType
from worker import Worker

#Represents a business 
class BusinessABC(WareStock, ABC):
	def __init__(self):
		super().__init__()
		self.businessType = BusinessType()
		self.staff = list([Worker()])

################################################################################
#IMPLEMENTATION

class Business(BusinessABC):
	def __str__(self):
		return str(self.businessType)

################################################################################
#TEST CODE

import unittest

class TestBusiness(unittest.TestCase):
	def test_attributes(self):
		t = Business()
		t.businessType
		t.staff[0]

if __name__ == "__main__":
	unittest.main(exit=False)