# Nathan Davis, 5/26/2020, Calculator project using Tkinter

import platform
import tkinter

if platform.python_version()[0] == '2':
	print("Please, switch to using python3 for better results.")
else:
	print("System Analysis:")
	print("\tUsing Python " + platform.python_version() +" on " +platform.system())
    
    
class Application(tk.Frame):
     def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()                               # define a function to create app elements
        
     def create_widgets(self):
     # we define a 
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello world\n"
        self.