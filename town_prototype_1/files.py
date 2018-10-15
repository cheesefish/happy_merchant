######################################
# Contains all data read from files. #
######################################

from ware import Ware
from production import ProductionIO
from production import Industry
from production import Agriculture

#######################################################
#FILE DATA

WARES = {} #dict of all loaded wares
AGRICULTURES = {} #dict of all loaded agricultures
INDUSTRIES = {} #dict of all loaded industries

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
    agricultures = [
            Agriculture("Apple farm", [ProductionIO("Apples",1)]),
            Agriculture("Grain farm", [ProductionIO("Grain",1)]),
            Agriculture("Hops farm", [ProductionIO("Hops",1)]),
            Agriculture("Cattle farm", [ProductionIO("Milk",5),ProductionIO("Beef",1)])
        ]
    for agriculture in agricultures:
        AGRICULTURES[str(agriculture)] = agriculture
        
def loadIndustriesTemp():
    industries = [
            Industry("Bakery", [ProductionIO("Grain",1)], [ProductionIO("Bread",1)],1),
            Industry("Brewery", [ProductionIO("Grain",1),ProductionIO("Hops",1)], [ProductionIO("Beer",1)],1),
            Industry("Dairy", [ProductionIO("Milk",1)], [ProductionIO("Butter",1),ProductionIO("Cheese",1)],1)
        ]
    for industry in industries:
        INDUSTRIES[str(industry)] = industry

#######################################################
#EXECUTION CODE
        
loadWaresTemp()
loadAgriculturesTemp()
loadIndustriesTemp()

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
