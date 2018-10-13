import sys
import time
import json

class Ware:
    def __init__(self, name, amount, production, production_cost, rating):
        self.name = name
        self.amount = amount
        self.price = 0
        self.production = production
        self.production_cost = production_cost
        self.rating = rating
       	

class Market:
    def __init__(self):
        self.wares = {}
    def update(self, town):
        for ware in self.wares.values():
            supply = ware.amount + ware.production
            ware.price = int(town.pop / (supply+1))
            if ware.price < 1:
           	    ware.price = 1
            demand = int(ware.rating / ware.price)
            ware.amount = supply - demand
            if ware.price <= ware.production_cost:
                ware.production = int(ware.production / 2)
            if ware.price > ware.production_cost:
                ware.production += 1

class Town:
    def __init__(self, name, pop, market):
        self.name = name
        self.pop = pop
        self.market = market

#################################################
#Test code:

#loads the first town in world.json
def loadTestTown():
    with open('world.json', 'r') as w:
	    world = json.load(w)
    
    first_town = world[0]['settlements'][0]
    name = first_town['name']
    pop = first_town['population']
    market = Market() 
    wares = []
    for i in first_town['wares']:
        wn = i['name']
        wa = i['amount']
        wp = i['production']
        wpc = i['production_cost']
        wr = i['rating']
        wares.append(Ware(wn,wa,wp,wpc,wr))
    
    for ware in wares:
        market.wares[ware.name] = ware
    return Town(name, pop, market)

def printMarketMenu(town):
    print(town.name, "Market")
    print("\tamount\tprice\tproduction")
    for ware in town.market.wares.values():
        print(ware.name + "\t" + str(ware.amount) + "\t" + str(ware.price) + "\t" + str(ware.production))

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
        
