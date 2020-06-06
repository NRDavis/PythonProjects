import shelve
shelfFile = shelve.open('mydata')		# returns shelve file object

# much like using a dictionary, we use a key to denote objects within our strucutre
shelfFile['cats'] = ['Zophie', 'pooka', 'Simon', 'Fat-tail']
shelfFile.close()


shelfFile = shelve.open('mydata')
a = shelfFile['cats']
print(a)
shelfFile.close()

'''

Allows us to store lists and dictionaries and data to a text file to be reopened in the future




'''