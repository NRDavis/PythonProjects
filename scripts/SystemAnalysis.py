# Nathan Davis, System Analysis, 5/26/2020
import platform
import sys
import os
from time import sleep
import ipaddress

import psutil

def printhead():
	print("---------------------------------------------------------------------------------------")
	print("System Analysis:")
	print("---------------------------------------------------------------------------------------")

def printoptions():
    print("Enter:\tMAIN(M)\t   USER(U)\tHARDWARE(H)\tSOFTWARE(S)\tNETWORK(N)\tQUIT(Q)\n")

def printmain():
    print("MAIN:")
    #print("Operating System\t\t\t"+platform.system())
    #print("Processor\t\t\t\t"+platform.processor())
    #print("Machine Tyspe\t\t\t"+platform.machine())  # same as processor
    uname = platform.uname()
    print("\t"+f"System: \t\t{uname.system}")
    print("\t"+f"Node Name: \t\t{uname.node}")
    print("\t"+f"Release: \t\t\{uname.release}")
    print("\t"+f"Version: \t\t{uname.version}")
    print("\t"+f"Machine: \t\t{uname.machine}")
    print("\t"+f"Processor: \t\t{uname.processor}")
    
    
def printhardware():
    print("HARDWARE:\n")
    print("\tCPU")
    print("\t\tCore Count\t\t "+ str(psutil.cpu_count())+"\tCores\t\t(QUAD)")
    
    cpufreq = psutil.cpu_freq()
    print("\t\tMax Frequency\t\t "+str((cpufreq.max))+" Mhz")
    print("\t\tMin Frequency\t\t "+str(cpufreq.min)+" Mhz")
    print(f"\t\tCurrent Frequency\t{cpufreq.current: .1f} Mhz")

    


def printsoftware():
    print("SOFTWARE:")
    #print("System Platform\t\t\t"+sys.platform())
    #print("Word length\t\t\t\t"+str(sys.getsizeof(int)))
    #print("PATH\t\t\t"+sys.path())


def printuser():
    print("USER:")

def printnetwork():
    print("NETWORK:")
    #print(ipaddress.IPv4Address())

def clear():
    #os.system()
    os.system("clear")
    printhead()
    printoptions()



# Initialize screen
clear()

# While loop system
i = 1
while(i != 0):
    q = input()
    if q == 'M' or q == 'm':
        clear()
        printmain()
    elif q == 'U' or q == 'u':
        clear()
        printuser()
    elif q == 'H' or q == 'h':
        clear()
        printhardware()
    elif q == 'S' or q == 's':
        clear()
        printsoftware()
    elif q == 'n' or q == 'N':
        clear()
        printnetwork()
    elif q == 'Q' or q == 'q':
        i = 0
        clear()
        print("QUIT() --- Program terminated.\n\n")
        sleep(2)
        os.system("clear")
