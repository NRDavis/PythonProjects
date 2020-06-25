# using oop with python

class point:
	x= 0
	y =0
	z =0
	
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		
	def ptPrint(self):
		print(str(self.x)+ " "+ str(self.y)+ " "+ str(self.z))
		
		
class line:
	a = point(0,0,0)
	b = point(0,0,0)
	
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	def LPrint(self):
		self.a.ptPrint()
		self.b.ptPrint()
		

k1 = point(1,1,1)
k2 = point(2,2,2)
L3 = line(k1,k2)
L3.LPrint()
