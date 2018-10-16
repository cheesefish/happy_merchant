#prototype of game logic

from files import TOWNS

def printMarketMenu(town):
    print(town.name, "Market")
    print("\tamount")
    for stock in town.market.stocks.values():
        print(str(stock) + "\t" + str(stock.amount))

def main():
    town = TOWNS["Aviv"]
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
        

