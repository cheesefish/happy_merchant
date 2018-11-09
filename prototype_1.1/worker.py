from abc import ABC, abstractmethod
from workertype import WorkerType

################################################################################
#ABSTRACT CODE

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

if __name__ == "__main__":
	Worker()
