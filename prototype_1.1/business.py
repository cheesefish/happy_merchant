from abc import ABC, abstractmethod
from warestock import WareStock
from businesstype import BusinessType

################################################################################
#ABSTRACTION

#Represents a business 
class BusinessABC(WareStock, ABC):
	def __init__(self):
		self.businessType = BusinessType()
		self.staff = list()

################################################################################
#IMPLEMENTATION

class Business(BusinessABC):
	def __str__(self):
		return str(self.businessType)

################################################################################
#TEST CODE

if __name__ == "__main__":
	Business()