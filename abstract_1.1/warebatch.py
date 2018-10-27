from wareamount import WareAmount

#WareBatch represents an amount of wares with the same perishability state.
class WareBatch(WareAmount):
	perishStatus = float() #Starts at 1.0 (100%) and is degraded over time.
	perishTimeLeft = int() #Countdown to next status degradation.

	#Decrements time left. When when time left reaches 0: reset time left and degrade status by specified amount (found in WareType).
	#When quality reaches 0: batch should be destroyed by caller; Raises exception.
	def updatePerishability(self): pass

	#Transfers amount to other batch from self. Sets perish stats of other to the lowest values between self and other.
	def transferToBatch(self, other, amount): pass

	#Transfers amount from other batch to self. Sets perish stats of self to the lowest values between self and other.
	def transferFromBatch(self, other, amount): pass

	#Returns dictionary key derived from waretype, perish status, and time passed.
	def key(self): pass
