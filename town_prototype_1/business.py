from stock import Stock
from stock import checkStockTransferability
from stock import transferStock
from stock import NegativeStockError

#Represents instances of certain industries, e.g. 'Bakery' or 'Brewery'.
class Business:
    def __init__(self, name, industry):
        self.name = str(name)
        self.industry = industry
        self.town = None
        self.stocks = {} #store of resources (industry's input-wares required for production of output-wares)
        self.fillAmounts = {} #desired amounts of stored resources
        self.effectiveThroughput = 0 #will change according to availability of stored resources
        for inpt in self.industry.inputs:
            key = str(inpt.ware)
            self.stocks[key] = Stock(inpt.ware, 0)
            self.fillAmounts[key] = inpt.amount
    def __str__(self):
        return self.name
    #Fills stored resources from market according to availability. Adapts effective throughput thereafter.
    def fillStocks(self):
        while self.effectiveThroughput < self.industry.throughput:
            try:
                for key in self.stocks:
                    checkStockTransferability(self.town.market.stocks[key], self.stocks[key], self.fillAmounts[key])
                for key in self.stocks:
                    transferStock(self.town.market.stocks[key], self.stocks[key], self.fillAmounts[key])
            except NegativeStockError:
                break
            self.effectiveThroughput += 1
    #Empties stored resources. Returns and resets effective throughput.
    def emptyStocks(self):
        for stock in self.stocks.values():
            stock.amount = 0
        tempEffectiveThroughput = self.effectiveThroughput
        self.effectiveThroughput = 0
        return tempEffectiveThroughput
        
            
#####################################################
#TEST CODE

from files import INDUSTRIES
if __name__ == "__main__":
    print("constructor/str test: ",end="")
    str(Business("",INDUSTRIES["Bakery"]))
    print("success-ish")
    
