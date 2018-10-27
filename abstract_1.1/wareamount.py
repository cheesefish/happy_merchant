from waretype import WareType

#A certain amount of a given ware. Usually doesn't represent 'real' goods. Rather represents e.g. input, output, or needs.
class WareAmount:
	wareType = WareType()
	amount = int()

	#Returns total weight (amount * waretype weight).
	def weight(self): pass

	#Transfers amount to other WareAmount from self.
	def transferTo(self, other, amount): pass

	#Transfers amount from other WareAmount to self.
	def transferFrom(self, other, amount): pass