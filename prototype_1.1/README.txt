PROTOTYPE 1.1 

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