class board:
	b = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
	
	def __init__(self):
		print("New board!")
		
	def printBoard(self):
		print(self.b["1"]+"|"+self.b["2"]+"|"+self.b["3"])
		print("_|_|_")
		print(self.b["4"]+"|"+self.b["5"]+"|"+self.b["6"])
		print("_|_|_")
		print(self.b["7"]+"|"+self.b["8"]+"|"+self.b["9"])
	
	
	def set(self, pos, mark):
		if self.writeCheck(pos):
			self.b[str(pos)] = mark
		
	def writeCheck(self, pos):
		if self.b[str(pos)] != " ":
			#print("Cannot overwrite position!")
			return False
		return True
		
	def winCheck(self):
		if self.b["1"] == self.b["2"] == self.b["3"]:
			if self.b["1"] != " ":
				return True
		elif self.b["4"] == self.b["5"] == self.b["6"]:
			if self.b["4"] != " ":
				return True
		elif self.b["7"] == self.b["8"] == self.b["9"]:
			if self.b["7"] != " ":
				return True
		elif self.b["1"] == self.b["4"] == self.b["7"]:
			if self.b["1"] != " ":
				return True
		elif self.b["2"] == self.b["5"] == self.b["8"]:
			if self.b["2"] != " ":
				return True
		elif self.b["3"] == self.b["6"] == self.b["9"]:
			if self.b["3"] != " ":
				return True
		elif self.b["1"] == self.b["5"] == self.b["9"]:
			if self.b["3"] != " ":
				return True
		elif self.b["3"] == self.b["5"] == self.b["7"]:
			if self.b["3"] != " ":
				return True
		else:
			return False


bb = board()
bb.printBoard() # printing out initial board
count = 1
while count < 10:
	
	print("next move:")
	p = input()
	
	if not bb.writeCheck(p):
		continue
	
	if count % 2 == 1:
		bb.set(p, "x")
	else:
		bb.writeCheck(p)
		bb.set(p,"o")
		
	if bb.winCheck():
		print("you win!!!")
		bb.printBoard()
		break
	print("\n"*30)
	bb.printBoard()
	count = count + 1
	if count == 10:
		print("no winner :(")
	