# walking a directory using python

import os

# os.walk returns 3 lists - one of the folder name, one of all the subfolders, and one of all the filenames 
for foldername, subfolders, filenames in os.walk(os.getcwd()):
    print('The folder is '+foldername)
    print('The subfolders in '+foldername+' are ' +str(subfolders))
    print('The filesnames in '+foldername+' are '+str(filenames))
    print()
