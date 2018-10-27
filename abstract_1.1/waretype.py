#WareType represents a type of tradable goods. There is exactly one unique instance of every type of Ware.
#The instances of WareType are loaded from file and kept in a dictionary with name as key.
class WareType:
	key = str() #Name of ware type. Used as dictionary key. Example names: "Bread", "Spices", "Weapons".
	weight = float() #physical weight of smallest unit of this ware
	perishStep = float() #e.g. 0.1
	perishTime = int() #number of ticks before quality degrades one step
