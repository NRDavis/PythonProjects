'''
	writing functions, pg 61-66
'''

def hello():
	print("Howdy")
	print("Hi")
	print("Hey")



hello()



def hiname(name):
    print("Hello, "+name)
    
hiname("Nathan")

# The print function may be modified to provide the exact output desired
print("Changing end of print character string from newline to_", end='_')
print()
print("Nathan", "Zoe", "Tex", sep='ABC')