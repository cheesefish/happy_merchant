from abc import ABC, abstractmethod
from wareamount import WareAmount

################################################################################
#ABSTRACT CODE

#WorkerType represents a type of worker. There is exactly one unique instance of every type of worker.
#The instances of WorkerType are loaded from file and kept in a dictionary with name as key.
class WorkerTypeABC(ABC):
	def __init__(self):
		self.key = str() #Name of worker type. Used as dictionary key. Example names: "Laborer", "Artisan", "Clerk".
		self.needs = list() #The consumption needs of a population.

################################################################################
#IMPLEMENTATION

class WorkerType(WorkerTypeABC):
	def __str__(self):
		return str(self.key)

################################################################################
#TEST CODE

if __name__ == "__main__":
	WorkerType()