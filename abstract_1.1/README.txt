ABSTRACT 1.1 
Abstract pseudo-code for the prototype 1.1 classes.

Note:
	- This folder contains no implemented code; only classes and their attributes and methods.
	- All attributes are typecasted, even if it doesn't make sense, just to show their types.

Structure:
	World
		Town
			Market(WareStock*)				
				WareBatch(WareAmount**)
			Agriculture
				FarmType
					WareAmount**
			Business(WareStock*)
				BusinessType
					WareAmount**
					WorkerType
						WareAmount**
				Worker
					WorkerType
						WareAmount**
			Population
				Household(WareStock*)
					Worker
						WorkerType
							WareAmount**
	*WareStock
		WareBatch(WareAmount**)
	**WareAmount
		WareType