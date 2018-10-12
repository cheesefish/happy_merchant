import sys
import time

class Ware:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.price = 0

class Market:
    def __init__(self):
        self.wares = {}
    def update(self, town):
        for ware in self.wares.values():
            #PRICE CALCULATION (SUPPLY/DEMAND)
            supply = ware.amount
            demand = town.pop
            ware.price = demand - supply
            if ware.price < 1:
                ware.price = 1

class Town:
    def __init__(self, name, pop, market):
        self.name = name
        self.pop = pop
        self.market = market

#################################################
#Test code:

def loadTestTown():
    name = "Aviv"
    pop = 1000
    market = Market()
    wares = [
            Ware("Bread", 1000),
            Ware("Beer", 1000),
            Ware("Grain", 1000),
            Ware("Honey", 1000),
            Ware("Cloth", 1000),
        ]
    for ware in wares:
        market.wares[ware.name] = ware
    return Town(name, pop, market)

def printMarketMenu(town):
    print(town.name, "Market")
    print("\tamount\tprice")
    for ware in town.market.wares.values():
        print(ware.name + "\t" + str(ware.amount) + "\t" + str(ware.price))

def main():
    town = loadTestTown()
    while True:
        town.market.update(town)
        printMarketMenu(town)
        order = input().strip()
        if "buy" in order[:4] or "sell" in order[:5]:
            try:
                name, amount = order[4:].strip().split(" ")
                ware = town.market.wares[name.capitalize()]
            except ValueError:
                print("failure: worng amount of arguments")
            except KeyError:
                print("failure: bad arguments")
            if "buy" in order[:4]:
                ware.amount -= int(amount)
            if "sell" in order[:5]:
                ware.amount += int(amount)
        print()

if __name__ == "__main__":
    main()
        
