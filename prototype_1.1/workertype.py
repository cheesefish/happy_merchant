#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from wareamount import WareAmount

#WorkerType represents a type of worker. There is exactly one unique instance of every type of worker.
#The instances of WorkerType are loaded from file and kept in a dictionary with name as key.
class WorkerTypeABC(ABC):
	def __init__(self):
		self.key = str() #Name of worker type. Used as dictionary key. Example names: "Laborer", "Artisan", "Clerk".
		self.needs = list([WareAmount()]) #The consumption needs of a population.

################################################################################
#IMPLEMENTATION

class WorkerType(WorkerTypeABC):
	def __str__(self):
		return str(self.key)

################################################################################
#TEST CODE

import unittest

class TestWorkerType(unittest.TestCase):
	def test_attributes(self):
		t = WorkerType()
		t.key
		t.needs[0]

if __name__ == "__main__":
	unittest.main(exit=False)
