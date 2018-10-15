from stock import Stock

#Represents the town market (each town has one).
class Market:
    def __init__(self, town):
        self.stocks = {}
        self.town = town
    #Adds new stocks to stock dictionary. Increments stock if it already is in the dictionary.
    def addStock(self, stock):
        key = str(stock)
        if key not in self.stocks:
            self.stocks[key] = stock
        else:
            self.stocks[key].amount += stock.amount
    #Updates stocks from production.
    def update(self):
        self._loadAgricuturalProduce()
        self._loadBusinessProducts()
        self._fillAllBusinessStocks()
    #Loads produce from town's agriculture, stores in market stocks.
    def _loadAgricuturalProduce(self):
        totalWeight = 0
        for agrialloc in self.town.agriallocs:
            totalWeight += agrialloc.weight
        for agrialloc in self.town.agriallocs:
            weightPercentage = agrialloc.weight / totalWeight
            for output in agrialloc.agriculture.outputs:
                amount = output.amount * self.town.acres * weightPercentage
                self.addStock(Stock(output.ware, amount))
    #Loads products from town's businesses, stores in market stocks.
    def _loadBusinessProducts(self):
        for business in self.town.businesses.values():
            throughput = business.emptyStocks()
            for output in business.industry.outputs:
                amount = output.amount * throughput
                self.addStock(Stock(output.ware, amount))
    #Restocks stores of town businesses.
    def _fillAllBusinessStocks(self):
        for business in self.town.businesses.values():
            business.fillStocks()
            
#####################################################
#TEST CODE

if __name__ == "__main__":
    print("constructor/str test: ",end="")
    str(Market(0))
    print("success")
