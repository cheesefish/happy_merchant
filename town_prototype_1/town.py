from market import Market

#Represents the amount of arable land that is allocated to a certain kind of agriculture, e.g. 'Cattle farming'.
class AgricultureAllocation:
    def __init__(self, agriculture, weight):
        self.agriculture = agriculture
        self.weight = weight #this allocation's part of the total allocation weight
    def __str__(self):
        return str(self.agriculture)

#Represents a settlement. Contains a market. Surrounded by arable land providing it with basic resources. Contains
#   artisan businesses.
class Town:
    def __init__(self, name, acres):
        self.name = str(name)
        self.acres = int(acres)
        self.market = Market(self)
        self.agriallocs = []
        self.businesses = {}
    def __str__(self):
        return self.name
    #Adds business to town's business dictionary. Guarantees unique key. Assigns town to business object.
    def addBusiness(self, business):
        key = business.name
        n = 1
        while True:
            if key in self.businesses:
                key = business.name + str(n)
                n += 1
            else:
                break
        self.businesses[key] = business
        business.town = self
    
#####################################################
#TEST CODE

if __name__ == "__main__":
    print("constructor/str test: ",end="")
    str(Town(0,0,0))
    print("success")
