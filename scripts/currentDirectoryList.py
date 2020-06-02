import os
import platform

print("playing around with our directory and operating system, os, module")
print(os.listdir(os.getcwd()))
print("")
print(          len(os.listdir(os.getcwd()))  )

    # The len() method allows us to check the length of a list
    # the os.listdir() method from os module allows us to obtain a list of all the files in our directory
    # the os.getcwd() method returns the current working directory 