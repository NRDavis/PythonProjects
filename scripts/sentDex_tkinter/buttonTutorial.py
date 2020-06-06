#sentdex tutorial -- tkinter gui 1
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()		# we call the create window function
   
	# creation of window
    def init_window(self):
        self.master.title('GUI')                            # set the title of the master widget
        self.pack(fill=BOTH, expand=1)              # allowing the widget to take the full space of root window
        quitButton = Button(self, text = 'Quit')      # creating button instance
        quitButton.place(x=0,y=0)                       # placing button on window 

root = Tk()

# size of wnidow
root.geometry('400x300')        # sets initial x and y dimensions
app = Window(root)
root.mainloop()