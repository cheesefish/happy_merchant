PROTOTYPE 1.1 

Class structure:
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

FILE TEMPLATE:
=================================
#<File Authors>
#Last edited: <dd-mm-yyyy>

################################################################################
#ABSTRACT CODE

from abc import ABC, abstractmethod
<other imports needed for abstract code>

#Class description
class ExampleClassABC(ABC):
	def __init__(self):
		self.vlaue = <type>() #Attribute description
		<...>

	#Method description
	@abstractmethod
	def exampleMethod(self, x, y): pass

	<...>

################################################################################
#IMPLEMENTATION

<imports needed for implementation>

class ExampleClass(ExampleClassABC):
	def exampleMethod(self, x, y):
		<implementation according to method description in abstract code>
	<...>

################################################################################
#TEST CODE

import unittest #no more imports should be necessary for testing

class TestExampleClass(unittest.TestCase):
	def test_exampleMethod(self):
		<test code>
	<...>

if __name__ == "__main__":
	unittest.main(exit=False)

========file template end========