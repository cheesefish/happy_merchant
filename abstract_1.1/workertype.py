from wareamount import WareAmount

#WorkerType represents a type of worker. There is exactly one unique instance of every type of worker.
#The instances of WorkerType are loaded from file and kept in a dictionary with name as key.
class WorkerType:
	key = str() #Name of worker type. Used as dictionary key. Example names: "Laborer", "Artisan", "Clerk".
	needs = list(WareAmount()) #The consumption needs of a population.