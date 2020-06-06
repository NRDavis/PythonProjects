'''
Author:						Nathan Davis
Date:						6.6.2020
Intent:						Create a simple desktop based application for providing QR Code creation and read services to students.
'''
#import tkinter as tk    # provides gui functionality
from tkinter import *
import qrcode
from time import time, asctime
from PIL import Image, ImageTk


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
        file.add_command(label='Import data')
        file.add_command(label='Generate QR Code', command=self.genQR('Nathan', 'Davis', 662))
        file.add_command(label="Exit",command=self.client_exit)     # we add exit command to file tab
        menu.add_cascade(label='File',menu=file)                            # we add the file tab to the menu

        edit = Menu(menu)
        #edit.add_command(label='Generate QR', command=self.genQR)
        #edit.add_command(label='Enter Student Information')
        menu.add_cascade(label='Edit',menu=edit)
    
    
        tools = Menu(menu)
        tools.add_command(label='plugin')
        menu.add_cascade(label='Tools', menu=tools)
    
        search = Menu(menu)
        search.add_command(label='Search')
        menu.add_cascade(label='Search Bar', menu=search)
    
    
    
    
    def genQR(self,firstName, lastName, ID):
        # we create a simple string using our studen'ts name, student ID, and the current time
        # In the following 12 lines, we create our qrcode as a png image 
        t = str(asctime())
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_M,
            box_size = 10,
            border = 4,
            )
        dataString = firstName +', '+lastName +' , ' +str(ID)+', '+t     # string concatenation of argument values 
        qr.add_data(dataString)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(firstName+lastName+"_qrcode.png") 
        
        # we read our newly created image and display it on the Window
        load = Image.open(firstName+lastName+'_qrcode.png')
        render = ImageTk.PhotoImage(load)
        image = Label(self, image = render)
        image.image = render
        image.place(x=0,y=0)
    
    def client_exit(self):
        exit()
        
root = Tk()
root.geometry('600x500')
app = Window(root)
root.mainloop()
    
