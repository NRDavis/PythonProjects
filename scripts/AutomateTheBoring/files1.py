'''
Files --- the python way


file name

file path       - the list of folders and sub folders a file is inside of 

root folders    C:\     ~/      etc
file extensions represent file type 

absolute file path  --- complete address of item
relative file path  --- path within root folder

.       this directory
..      parent folder 

'''

filePath = 'C:\\spam\\eggs.png'        # we must escape characters -- this only works on windows
print(filePath)

import os           # import operating system module

        # returns the string value of a path appropriate for the operating system we're using
a = os.path.join('folder1','folder2','folder3','file.png')
print(a)

# os.sep variable -- used to store which character we're using for the relevant operating system

print(os.getcwd())      # get the current working directory

#os.chdir("input/string")      # change the current working directory depending upon input string

print(os.path.abspath('files1.py'))     # returns absolute path of file 
#os.path.isabs()      # determines if a string passed in is a legit file path
#os.path.relpath("folder/folder/spam.png", "1'')

#os.path.dirname()              pulls out the directory name, leaving the file name 
#os.path.basename()         pulls out individual file names, of the last folder name 
# os.path.exists()              returns true if file name actually exists
print(os.path.exists(os.getcwd()+'/files1.py'))

print(os.path.isfile(os.getcwd()+'/files1.py'))    # checks for file name 
print(os.path.isdir(os.getcwd()+'/files1.py'))

# os.path.getsize()     # returns byte size integer
# os.listdir()              # resturns the contents of a directory, and it returns list of strings with files names and folder names

# os.makedirs()     # pass path, abs or relative and itll make that