'''
Name:			Nathan Davis
Date:			6.27.2020

Historic Stock Analysis Software
'''

# setting up the GUI
import tkinter as tk
from tkinter import font as tkfont

import pages.homepage as hp
import pages.settingspage as sp

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.minsize(960, 720)
        self.maxsize(960,720)
        #self.config(bg='skyblue')
       
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight = 'bold', slant='italic')
        self.title("Historic Stock Analysis")
        
        container = tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        #sp.StartPage, po.PageOne, pt.PageTwo,
        
        self.frames={}
        for F in (hp.HomePage, sp.SettingsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame 
            frame.grid(row=0, column=0, sticky='new')
        
        self.show_frame("HomePage")
        
    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
        menubar = frame.menubar(self)           # used to implement the menu bars for each frame page
        self.configure(menu=menubar)            # configure the menubar
  
  
if __name__ == "__main__":
    app = App()
    app.mainloop()        
        
        
