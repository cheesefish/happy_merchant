from warestock import WareStock
from businesstype import BusinessType

#Represents a business 
class Business(WareStock):
	businessType = BusinessType()
	staff = list(Worker())