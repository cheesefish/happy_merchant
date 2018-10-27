from farmtype import FarmType

#Represents the agricultural production of a town.
class Agriculture:
	acres = int() #arable land available to town in acres
	farmtypes = list(FarmType()) #types of wares farmed on town's arable land
	percent = list(float()) #precentage of each ware type farmed out of arable land