from warebatch import WareBatch

#Represents a collection of ware batches, an inventory; e.g. market, business, or personal inventory. 
class WareStock:
	batches = dict(WareBatch())

	#Updates all batches' perishability stats.
	def updatePerishabilities(self): pass

	#Resets perish stats of all batches to their full states.
	#Used by some stocks (e.g. markets) that doesn't deal with perishability.
	def resetPerishabilities(self): pass

	#Merges all batches of same type.
	def mergeBatches(self): pass
