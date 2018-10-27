from waretype import WareType
from warestock import WareStock
from warebatch import WareBatch

#Represents the central trading hub of a town. Functions as a town inventory where goods are gathered and distributed.
#Transactions require equal exchange, even for local actors such as population and businesses.
class Market(WareStock):
	exchangeOffers = list(WareBatch())
	exchangeDemands = list(WareBatch())

	#Returns price of ware in default currency (WareType). Choose other currency by calling: "market.getPriceOf(wareAmount).inCurrency(otherWareType)".
	def getPriceOf(self, batch, amount): pass

	#Cleans up exchange data, resetting any ongoing exchange.
	def resetExchange(self): pass

	#Adds new batch to exchange offers.
	def offerToExchange(self, batch, amount): pass

	#Adds new batch to demand offers.
	def demandFromExchange(self, batch, amount): pass

	#Returns price balance of exchange. Positive means you have offered more value than demanded; negative means you have demanded more value than offered.
	def getExchangeBalance(self): pass

	#Returns demanded batches. Transfers offered batches. Resets exchange. Raises Exception if exchange balance is negative (the market isn't a charity, goyim!).
	def proposeExchange(self): pass

#Represents price. Is used simply as a float but contains data to enable recalculation in another currency.
class Price(float):
	market = Market() #Market that created price.
	currency = WareType() #The ware that this price if based on. E.g. Copper coin, Silver coin, etc.

	#Returns self. Changes price value according to value relation between old and new currency. 
	def inCurrency(self, wareType): pass