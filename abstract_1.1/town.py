from market import Market
from agriculture import Agriculture
from businesses import Business
from population import Population

class Town:
	market = Market()
	agriculture = Agriculture()
	businesses = list(Business())
	population = Population()

	#User interface of town.
	def ui(self): pass