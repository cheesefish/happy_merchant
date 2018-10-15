#An instance of Ware represents a certian tradable goods type, e.g. 'Apples' or 'Wine', and contains some basic
#information about that particular type.
class Ware:
    def __init__(self, name):
        self.name = str(name)
        #CAN ADD MORE ATTRIBUTES LATER ON (ex. base price, weight, etc.)
    def __str__(self):
        return self.name

#####################################################
#TEST CODE

if __name__ == "__main__":
    print("constructor/str test: ",end="")
    str(Ware(""))
    print("success")
