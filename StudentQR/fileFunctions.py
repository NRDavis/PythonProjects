'''
Author:						Nathan Davis
Date:						6.6.2020
Filename:					fileFunctions.py		
'''
from time import time
import qrcode
from tkinter import *

#class Window(Frame):

def client_exit(self):
    exit()


def genQR(firstName, lastName, ID, Time):
    # we create a simple string using our studen'ts name, student ID, and the current time
    t = str(time.time())
    
    qr = qrcode.QRCODE(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_M,
        box_size = 10,
        border = 4,
        )
        dataString = FirstName +', '+lastName +' , ' +str(ID)+', '+t     # string concatenation of argument values 
        img = qr.make_image()
        img.save(firstName+lastName+"_qrcode.jpg") 