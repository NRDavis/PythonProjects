#menubar.py


from tkinter import *

#create class, Window, and inherit from the Frame class
class Window(Frame):
    #Define settings upon initialization
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class
        Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master
        # with that, we want to run init_window()
        self.init_window()
        
        
    def init_window(self):
        #changing the title of our master widget
        self.master.title("GUI")
        #allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        #creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        #create the file object
        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)    #
        menu.add_cascade(label='File',menu=file)        # added file to our menu 
        
        edit = Menu(menu)
        #adds a command to the menu option
        edit.add_command(label='Undo')
        #added file to our menu
        menu.add_cascade(label='Edit', menu=edit)
        
    def client_exit(self):
        exit()
        
        
# create root window
root = Tk()
root.geometry('400x300')
app = Window(root)
# mainloop
root.mainloop()