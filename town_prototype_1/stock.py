#Error that is raised when a given stock amount argument is negative.
class NegativeAmountError(Exception):
	pass

#Error that is raised when a stock transfer involves two different wares.
class StockTypeError(Exception):
	pass

#Error that is raised when a stock transfer results in the transferer stock becoming negative.
class NegativeStockError(Exception):
	pass

#A stock is a certain amount of a certain ware. Represents a stock of goods in the market or in a business.
class Stock:
	def __init__(self, ware, amount):
		self.ware = ware
		if amount < 0:
			raise NegativeAmountError()
		self.amount = int(amount)
	def __str__(self):
		return str(self.ware)
	#Transfers from other stock to self
	def transferFromStock(self, stock, amount):
		checkStockTransferability(stock, self, amount)
		transferStock(stock, self, amount)
	#Transfers from self to other stock
	def transferToStock(self, stock, amount):
		checkStockTransferability(self, stock, amount)
		transferStock(self, stock, amount)

#Raises exceptions if a transfer contains bad arguments or results in an bad state.
def checkStockTransferability(fromStock, toStock, amount):
	if amount < 0:
		raise NegativeAmountError()
	if fromStock.ware != toStock.ware:
		raise StockTypeError()
	if fromStock.amount < amount:
		raise NegativeStockError()

#Transfers the given amount from one stock to the other. Can result in a bad state (negative stock amounts).
def transferStock(fromStock, toStock, amount):
	fromStock.amount -= int(amount)
	toStock.amount += int(amount)

#####################################################
#TEST CODE

if __name__ == "__main__":
	print("constructor/str test: ",end="")
	str(Stock(0,0))
	print("success")
	
	ware1 = "dummyware1"
	ware2 = "dummyware2"

	#transferToStock test
	print("test1: ",end="")
	stock1 = Stock(ware1, 5)
	stock2 = Stock(ware1, 5)
	stock1.transferToStock(stock2, 5)
	if stock1.amount == 0 and stock2.amount == 10:
		print("success")
	else:
		print("ERROR")

	#transferFromStock test
	print("test2: ",end="")
	stock1.transferFromStock(stock2, 5)
	if stock1.amount == 5 and stock2.amount == 5:
		print("success")
	else:
		print("ERROR")

	#negative amount argument test
	print("test3: ",end="")
	stock1 = Stock(ware1, 5)
	stock2 = Stock(ware2, 5)
	try:
		transferStock(stock1, stock2, -1)
		print("ERROR")
	except NegativeAmountError:
		print("success")

	#differing stock types (wares) test
	print("test4: ",end="")
	try:
		transferStock(stock1, stock2, 0)
		print("ERROR")
	except StockTypeError:
		print("success")

	#testing transfer that results in a bad state (negative stock)
	print("test5: ",end="")
	stock2 = Stock(ware1,5)
	try:
		transferStock(stock1, stock2, 6)
		print("ERROR")
	except NegativeStockError:
		print("success")
	
