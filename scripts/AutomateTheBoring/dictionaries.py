# introduction to dictionary data types

'''
indices for dictionaries are called keys- for key/value pairs

disctionaries are unordered, unline lists



'''

myCat = {'size':'fat',
            'color':'gray',
            'disposition':'loud'}


print("Our dictionary "+str(myCat))

print("My cat has "+myCat['color']+' fur.')


eggs = {'name': 'zophie', 'species':'cat', 'age':8}
ham = {'species':'cat', 'name':'zophie', 'age':8}
print('eggs == ham: '+str(eggs == ham))
print('There is a name element in our egg\'s dictionary: '+str('name' in eggs)) # checking that e is a index by the name of name in our dictionary
print("The value of cat exists within our eggs dictionary: "+str('cat' in eggs.values()))


if 'color' not in eggs:
    eggs['color'] = 'black' # we add item if it does not already exist

eggs.setdefault('color','orange')   # if the element already exists, then nothing changes, else it is defauted to orange
