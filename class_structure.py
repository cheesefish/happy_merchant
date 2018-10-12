class Ware:
    #ATTRIBUTES:
    #str name       
    #int amount
    #int price      Determined by demand.
    pass

class Market:
    #ATTRIBUTES:
    #dict wares     List of Ware-objects, representing the market's supply of goods.
    
    def update(self, town):
        #Updates the market supply and prices according to the town's population and industry.
        pass

class Industry:
    #ATTRIBUTES:
    #dict output     List of Ware-objects, representig the industry's throughput of goods.
    pass

class Town:
    #ATTRIBUTES:
    #str name
    #int pop            Town population number
    #Market market
    #Industry industry
    pass

class World:
    #ATTRIBUTES:
    #dict towns
    pass

