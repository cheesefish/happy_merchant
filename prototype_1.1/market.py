from abc import ABC, abstractmethod
from waretype import WareType
from warestock import WareStock
from warebatch import WareBatch

################################################################################
#ABSTRACTION

#Represents the central trading hub of a town. Functions as a town inventory where goods are gathered and distributed.
#Transactions require equal exchange, even for local actors such as population and businesses.
class MarketABC(WareStock, ABC):
	def __init__(self):
		self.exchangeOffers = list()
		self.exchangeDemands = list()

	#Returns price of ware in default currency (WareType). Choose other currency by calling: "market.getPriceOf(wareAmount).inCurrency(otherWareType)".
	@abstractmethod
	def getPriceOf(self, batch, amount): pass

	#Cleans up exchange data, resetting any ongoing exchange.
	@abstractmethod
	def resetExchange(self): pass

	#Adds new batch to exchange offers.
	@abstractmethod
	def offerToExchange(self, batch, amount): pass

	#Adds new batch to demand offers.
	@abstractmethod
	def demandFromExchange(self, batch, amount): pass

	#Returns price balance of exchange. Positive means you have offered more value than demanded; negative means you have demanded more value than offered.
	@abstractmethod
	def getExchangeBalance(self): pass

	#Returns demanded batches. Transfers offered batches. Resets exchange. Raises Exception if exchange balance is negative (the market isn't a charity, goyim!).
	@abstractmethod
	def proposeExchange(self): pass

################################################################################
#IMPLEMENTATION

class Market(MarketABC):
	pass

#Represents price. Is used simply as a float but contains data to enable recalculation in another currency.
class Price(float):
	def __init__(self, market):
		self.market = market #Market that created price.
		self.currency = WareType() #The ware that this price if based on. E.g. Copper coin, Silver coin, etc.

	#Returns self. Changes price value according to value relation between old and new currency.
	def inCurrency(self, wareType): pass

################################################################################
#TEST CODE

if __name__ == "__main__":
	m = Market()
	Price(m)