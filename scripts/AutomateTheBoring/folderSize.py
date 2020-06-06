import os

totalSize = 0
for filename in os.listdir(os.getcwd()):		# we iterate through the files in our current working directory
    if not os.path.isfile(os.path.join(os.getcwd(), filename)):
        continue
    totalSize = totalSize + os.path.getsize(filename)

print(totalSize)            # returns total size of our folder in bytes