# copying files
import os
import shutil

# we write to a file
writeFile = open(os.getcwd()+'/copy1.txt', 'w')
writeFile.write('This is cool!\nYeet!\n')
writeFile.close()

os.makedirs(os.getcwd()+'/copyFolder')


# we copy the file to a directory we allocate within the cwd
shutil.copy(os.getcwd()+'/copy1.txt', os.getcwd()+'/copyFolder/copy2.txt')
        # we also rename the file to copy2.txt 

# shutil.copytree(copy-folder, new folder)


#shutil.move(file-to-move, new-location)


  