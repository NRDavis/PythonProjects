import tkinter as tk
from tkinter import font as tkfont 


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent 
        
        label = tk.Label(self, text = 'Settings Page', font = controller.title_font).grid(row=0, column = 0, padx=10, pady=5, ipadx=10, ipady=5)
        
    def menubar(self, root):
        menubar = tk.Menu(root)
        
        File = tk.Menu(menubar)
        File.add_command(label='Home', command=lambda:self.controller.show_frame("HomePage"))
        File.add_command(label="Exit", command=self.client_exit)
        menubar.add_cascade(label="File",menu=File)
        
        Edit = tk.Menu(menubar)
        Edit.add_command(label="Edit")
        menubar.add_cascade(label="Edit",menu=Edit)
        return menubar
        
    def client_exit(self):
        exit()
        