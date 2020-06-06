#eventhandling.py
from tkinter import *

# create class, Window, and inherit from the frame class
# Frame is a class from the Tkinter module

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)    # we initialize our frame -- allocate a reference
        self.master = master            # reference to the master widget, the tk window
        self.init_window()          # we initialize our window
         
    # creation of init_window
    def init_window(self):
        #changing the title of our master widget
        self.master.title("GUI")
        #allow the widget to take the full space of the root window 
        self.pack(fill=BOTH, expand=1)
        #creating a button instance
        quitButton = Button(self, text='Exit', command=self.client_exit)
        #placing the button on my window 
        quitButton.place(x=0,y=0)
        
    def client_exit(self):
        exit()                          # we exit the program upon pressing the button
        
# root window created. Here, that would be the only window, but
# you can later have windows within windows
root = Tk()
root.geometry('400x300')
#creation of an instance
app = Window(root)
#mainloop
root.mainloop()