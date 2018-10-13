WARES = {}

class UnknownProductionType(Exception):
    pass

class Ware:
    def __init__(self, name, productionType):
        self.name = str(name)
        self.prodtype = str(productionType)
        if productionType != "basic" and productionType != "artisan":
            raise UnknownProductionType(productionType)
        #CAN ADD MORE ATTRIBUTES LATER ON (ex. base price, weight, etc.)
    def __str__(self):
        return self.name

#TEMPORARY; TODO: implement json
def loadWares(filename):
    with open(filename, "r") as file:
        for row in file.readlines():
            if not row[0] == "#":
                row = row.strip().split(";")
                WARES[row[0]] = Ware(row[0],row[1])
                
loadWares("tempwares.txt")

#TEST CODE
if __name__ == "__main__":
    for ware in WARES:
        print(ware,end=";")
        print(WARES[ware].prodtype)
