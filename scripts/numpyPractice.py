import numpy as np

a = np.array([[1,2,3],[4,5,6]]) 

print('First array:')
print(a)
print('\n')

print('Append elements to array:')
print(np.append(a, [7,8,9]) )
print('\n')

print('Append elements along axis 0:')
print(np.append(a, [[7,8,9]],axis = 0) )
print('\n')

a =np.append(a, [7,8,9]) # we have to reassign items
print(a)

a = np.append(a, [10,11,12], axis=0)
print(a)