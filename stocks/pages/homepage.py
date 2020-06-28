import tkinter as tk
from tkinter import font as tkfont 
from PIL import Image, ImageTk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.parent.config(bg='#000000')        # this works for changing the background color of the frame
        
        label = tk.Label(self, text='Home', font = controller.title_font).grid(row=0,column=0, padx=10, pady=5, ipadx=10, ipady=5)
       
        label = tk.Label(self, text='search').grid(row=1,column=0, padx=0, pady=0, ipadx=0, ipady=0)
        searchbar = tk.Entry(self).grid(row=1,column=1)
        
        #tk.Button(self, text="Go back to settings page", command=lambda: self.parent.switch_frame(SettingsPage)).grid()
        
    def menubar(self, root):
        menubar = tk.Menu(root)
        
        File = tk.Menu(menubar)
        File.add_command(label='settings', command=lambda:self.controller.show_frame("SettingsPage"))
        File.add_command(label="Exit", command=self.client_exit)
        menubar.add_cascade(label="File",menu=File)
        
        Edit = tk.Menu(menubar)
        Edit.add_command(label="Edit")
        menubar.add_cascade(label="Edit",menu=Edit)
        return menubar
        
        
    def client_exit(self):
        exit()
        