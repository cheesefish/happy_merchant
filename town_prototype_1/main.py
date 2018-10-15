#prototype of game logic

from files import INDUSTRIES
from files import AGRICULTURES
from town import Town
from town import AgricultureAllocation
from business import Business

def loadTestTown():
    name = "Aviv"
    acres = 1000
    town = Town(name, acres)
    for agriculture in AGRICULTURES.values():
        town.agriallocs.append(AgricultureAllocation(agriculture, 1))
    businesses = [
            Business("Joe's Bakery", INDUSTRIES["Bakery"]),
            Business("Bob's Bakery", INDUSTRIES["Bakery"]),
            Business("Ye Olde Brewery", INDUSTRIES["Brewery"]),
            Business("The Cheese & Butter Company", INDUSTRIES["Dairy"])
        ]
    for business in businesses:
        town.addBusiness(business)
    return town

def printMarketMenu(town):
    print(town.name, "Market")
    print("\tamount")
    for stock in town.market.stocks.values():
        print(str(stock) + "\t" + str(stock.amount))

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
        
main()
        

