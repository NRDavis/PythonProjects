

class contact:
	name = ""
	phone = ""
	email =""
	def __init__(self, n,  p, e=""):
		self.name = n
		self.phone = p
		self.email = e
		
	def getName(self):
		return self.name
		
	def printName(self):
		print(self.name)
		
	def setName(self,n):
		self.name = n
		
	def getPhone(self):
		return self.phone
		
	def setPhone(self, p):
		self.phone = p
		
	def printPhone(self):
		print(self.phone)
		
	def setEmail(self, e):
		self.email = e
		
	def getEmail(self):
		return self.email
		
	def printEmail(self):
		print(self.email)
		
	def contactPrint(self):
		print(self.name)
		print(self.phone)
		print(self.email)

a = contact("Nerd", "(252)889-4567")
a.contactPrint()

b = contact("2ndPerson","919-234-7888","2nd@email.com")
b.contactPrint()