# list methods

spam = ['hello','hi','howdy','heyas']
a = spam.index('hello')         # returns the index value of the item within the list, exception if not found
#print(a)            # returns first instance

scam = ['cat', 'dog', 'bat']
scam.append('moose')
scam.insert(1, 'chicken')
print(scam)
scam.remove('chicken')  # allows use to remove the chicken item without reference to its index
print(scam)
del scam[2]
print(scam)



pam = [1,5,3,4]
print(pam)
pam.sort()
print(pam)
pam.sort(reverse=True)
print(pam)


abc = list('hello')
print(abc)

name = 'Zoe'
print('Zo' in name)

for letter in name:
    print(letter)
    
import copy
cheese = copy.deepcopy(name)
print(cheese)       # deepcopy creates an entirely new, separate copy of our list

print("Four score and seven + \
    years ago")


