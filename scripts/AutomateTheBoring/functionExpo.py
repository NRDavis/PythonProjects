
'''
built in functions

print()
input
len()
str()


standard library
	math module has math functions
	etc, etc

 

'''

import sys, os, math            # importing multiple modules in a single line
#import random       # import module to gain access to functions 
#random.randint(1, 10)	# returns a random integer between low and high boundaries

from random import *        # allows us to import all of the items from random module - provides scope
randint(1,10)

sys.exit()      # causes the program to end -- nothing after this is printed


import pyperclip                    # 3rd party module for copying text - useful for program input
pyperclip.copy('Hello World!')
pyperclip.paste()

