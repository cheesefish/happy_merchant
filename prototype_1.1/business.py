from abc import ABC, abstractmethod
from warestock import WareStock
from businesstype import BusinessType

################################################################################
#ABSTRACT CODE

#Represents a business 
class BusinessABC(WareStockABC, ABC):
	def __init__(self):
		self.businessType = BusinessTypeABC()
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