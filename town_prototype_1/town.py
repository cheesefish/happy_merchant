from wares import WARES

class Stock:
    def __init__(self, name, amount, production, production_cost, rating):
        self.ware = WARES[name]
        self.amount = int(amount)
        self.price = 0
        self.production = production
        self.production_cost = production_cost
        self.rating = rating
    def __str__(self):
        return str(self.ware)

class Market:
    def __init__(self):
        self.stocks = {}
        self.town = None
    def update(self):
        for stock in self.stocks.values():
            self.__updatePrice(stock)
    def __updatePrice(self, stock):
        supply = stock.amount + stock.production
        stock.price = int(self.town.pop / (supply+1))
        if stock.price < 1:
            stock.price = 1
        demand = int(stock.rating / stock.price)
        stock.amount = supply - demand
        if stock.price <= stock.production_cost:
            stock.production = int(stock.production / 2)
        if stock.price > stock.production_cost:
            stock.production += 1
                
class Town:
    def __init__(self, name, pop, market):
        self.name = name
        self.pop = pop
        self.market = market
        market.town = self
   
#################################################
#Test code:
        
def loadTestTown():
    name = "Aviv"
    pop = 1000
    market = Market()
    stocks = [
            Stock("Bread", 0, 0, 20, 40),
            Stock("Beer", 0, 0, 50, 90),
            Stock("Grain", 0, 0, 10, 20),
            Stock("Honey", 0, 0, 30, 70),
            Stock("Cloth", 0, 0, 40, 30),
        ]
    for stock in stocks:
        market.stocks[str(stock)] = stock
    return Town(name, pop, market)

def printMarketMenu(town):
    print(town.name, "Market")
    print("\tamount\tprice\tproduction")
    for stock in town.market.stocks.values():
        print(str(stock) + "\t" + str(stock.amount) + "\t" + str(stock.price) + "\t" + str(stock.production))

def main():
    town = loadTestTown()
    while True:
        town.market.update()
        printMarketMenu(town)
        order = input().strip()
        if "buy" in order[:4] or "sell" in order[:5]:
            try:
                name, amount = order[4:].strip().split(" ")
                stock = town.market.stocks[name.capitalize()]
            except ValueError:
                print("failure: worng amount of arguments")
            except KeyError:
                print("failure: bad arguments")
            if "buy" in order[:4]:
                stock.amount -= int(amount)
            if "sell" in order[:5]:
                stock.amount += int(amount)
        print()

if __name__ == "__main__":
    main()
        

