# deleting files
import os
os.unlink(os.getcwd()+'/copy1.txt')		# permanently deletes file


# os.rmdir('pass-folder')       # removes folder - folder must be empty, prevents deletion of valuable info
# shutil.rmtree()           # will remove a folder and all its contents

        # listdir() returns a list of strings for each file name
for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlinked(filename)

# can install send2trash
# send2trash.send2trash(path)