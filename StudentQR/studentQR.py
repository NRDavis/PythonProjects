'''
Author:						Nathan Davis
Date:						6.6.2020
Intent:						Create a simple desktop based application for providing QR Code creation and read services to students.
'''
#import tkinter as tk    # provides gui functionality
from tkinter import *
#import qrcode           # used to generate QR Codes
from qrcode import *
#from fileFunctions import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("StudentQR")
        self.pack(fill=BOTH,expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)           # we create file tab
        
        
        #file.add_command(label='Import Student CSV', command=self.readCSV)  # read information from a CSV list
        #file.add_command(label='Generate QR Code', command=self.genQR)
        file.add_command(label="Exit",command=self.client_exit)     # we add exit command to file tab
        menu.add_cascade(label='File',menu=file)                            # we add the file tab to the menu

        edit = Menu(menu)
        #edit.add_command(label='Generate QR', command=self.genQR)
        #edit.add_command(label='Enter Student Information')
        menu.add_cascade(label='Edit',menu=edit)
    
    
    
    
    def client_exit(self):
        exit()
        
root = Tk()
root.geometry('600x500')
app = Window(root)
root.mainloop()
    
