#Karl Lindgren
#Last edited: 09-11-2018

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
from workertype import WorkerTypeABC

#Represents a single worker.
class WorkerABC(ABC):
	def __init__(self):
		self.workerType = WorkerTypeABC() #Profession of the worker.
		self.experience = float() #Experience of worker.

################################################################################
#IMPLEMENTATION

class Worker(WorkerABC):
	def __str__(self):
		return str(self.workerType)

################################################################################
#TEST CODE

import unittest

class TestWorker(unittest.TestCase):
	def test_attributes(self):
		t = Worker()
		t.workerType
		t.experience

if __name__ == "__main__":
	unittest.main(exit=False)
