#playing with classes

class test:
	integer = 0
	double = 0.0
	
	def __init__(self, i, x):
		self.integer = i
		self.double =x
		
	def testPrint(self):
		print(str(self.integer)+" "+str(self.double))
		
		
		
a = test(2, 4)
a.testPrint()