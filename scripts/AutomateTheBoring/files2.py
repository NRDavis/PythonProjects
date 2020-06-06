'''

Writing plaintext files
.txt files              (just text)

with python scripts

Can also write binary files 



We can save variables, data structures, etc using the shelve module





'''
import os

helloFile = open(os.getcwd()+'/hello.txt')      # we open files for ubuntu system, in read mode - can only read, no modification
s = helloFile.read()    # you can only ead once - to read again you must helloFile.close() and call open again 
print(s)
helloFile.close()

howdyFile = open(os.getcwd()+'/howdy.txt')
W = howdyFile.readlines()    # reads line by line and allocates list of strings 
print(W[:])
howdyFile.close()
# .readline()   method reads a single line at a time

# to write a fresh file, pass open() the 'w' argument following the path
# to open in append mode, pass open the 'a' argument    -- in both 'w' and 'a' cases, if the file doesnt exist, it will be created upon being called

hello2File = open(os.getcwd()+'/hello2.txt', 'w')
hello2File.write("Hello!!!!!!!!!")      # doesnt allocate newlines - must add those in manually
hello2File.close()