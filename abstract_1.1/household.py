from warestock import WareStock
from worker import Worker

#Represents a population unit, with its own inventory and a main provider.
class Household(WareStock):
	worker = Worker() #Main provider of household.
	size = int() #Number of people in the household.
