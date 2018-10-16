#Represents the input OR output flow in a production (industry/agriculture).
class ProductionIO:
    def __init__(self, ware, amount=1):
        self.ware = ware
        self.amount = float(amount)

#Represents rural 'industry' types (production of basic resources, based on arable land area). Farming.
class Agriculture:
    def __init__(self, name, outputs):
        self.name = str(name)
        self.outputs = outputs #outputs = [ProductionIO(ware, amount),...]
    def __str__(self):
        return self.name

#Represents urban industry types (refining of basic resources). Artisan based production.
class Industry:
    def __init__(self, name, inputs, outputs, throughput):
        self.name = str(name)
        self.inputs = inputs #inputs = [ProductionIO(ware, amount),...]
        self.outputs = outputs #outputs = [ProductionIO(ware, amount),...]
        self.throughput = float(throughput)
    def __str__(self):
        return self.name
    
#####################################################
#TEST CODE

if __name__ == "__main__":
    print("constructor/str test: ",end="")
    ProductionIO(0)
    str(Industry(0,0,0,0))
    str(Agriculture(0,0))
    print("success")
