######################################
# Contains all data read from files. #
######################################

from ware import Ware
from production import ProductionIO
from production import Industry
from production import Agriculture
from town import Town
from town import AgricultureAllocation
from business import Business

#######################################################
#FILE DATA

WARES = {} #dict of all loaded wares
AGRICULTURES = {} #dict of all loaded agricultures
INDUSTRIES = {} #dict of all loaded industries
TOWNS = {} #dict of all loaded towns

#######################################################
#READ FUNCTIONS

def loadWaresTemp():
    wares = [
            Ware("Apples"),
            Ware("Grain"),
            Ware("Hops"),
            Ware("Milk"),
            Ware("Beef"),
            Ware("Bread"),
            Ware("Beer"),
            Ware("Butter"),
            Ware("Cheese")
        ]
    for ware in wares:
        WARES[str(ware)] = ware

def loadAgriculturesTemp():
    k = 0.001
    agricultures = [
            Agriculture("Apple farm", [ProductionIO("Apples",k*10)]),
            Agriculture("Grain farm", [ProductionIO("Grain",k*15)]),
            Agriculture("Hops farm", [ProductionIO("Hops",k*10)]),
            Agriculture("Cattle farm", [ProductionIO("Milk",k*10),ProductionIO("Beef",k*5)])
        ]
    for agriculture in agricultures:
        AGRICULTURES[str(agriculture)] = agriculture
        
def loadIndustriesTemp():
    industries = [
            Industry("Bakery", [ProductionIO("Grain",1)], [ProductionIO("Bread",1)],1),
            Industry("Brewery", [ProductionIO("Grain",10),ProductionIO("Hops",5)], [ProductionIO("Beer",1)],0.1),
            Industry("Dairy", [ProductionIO("Milk",1)], [ProductionIO("Butter",1),ProductionIO("Cheese",1)],1)
        ]
    for industry in industries:
        INDUSTRIES[str(industry)] = industry

def loadTestTownTemp():
    name = "Aviv"
    acres = 1000
    town = Town(name, acres)
    agriallocs = [
            AgricultureAllocation(AGRICULTURES["Apple farm"], 10),
            AgricultureAllocation(AGRICULTURES["Grain farm"], 50),
            AgricultureAllocation(AGRICULTURES["Hops farm"], 20),
            AgricultureAllocation(AGRICULTURES["Cattle farm"], 20)
        ]
    town.agriallocs = agriallocs
    businesses = [
            Business("Joe's Bakery", INDUSTRIES["Bakery"]),
            Business("Bob's Bakery", INDUSTRIES["Bakery"]),
            Business("Ye Olde Brewery", INDUSTRIES["Brewery"]),
            Business("The Cheese & Butter Company", INDUSTRIES["Dairy"])
        ]
    for business in businesses:
        town.addBusiness(business)
    TOWNS[name] = town
    
#######################################################
#EXECUTION CODE
        
loadWaresTemp()
loadAgriculturesTemp()
loadIndustriesTemp()
loadTestTownTemp()

#######################################################
#TEST CODE

if __name__ == "__main__":
    tab = " "
    print("Wares:")
    for ware in WARES:
        print(tab + str(ware))
    print()
    print("Agricultures:")
    for agriculture in AGRICULTURES:
        print(tab + str(agriculture))
    print()
    print("Industries:")
    for industry in INDUSTRIES:
        print(tab + str(industry))
    print()
