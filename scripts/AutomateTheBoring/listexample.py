

spam = ["cat", 'bat', 'rat', 'elephant']

#print('spam[0] = '+spam[0])

for i in range(0,4):
    print("spam["+str(i)+"] = "+spam[i])
    
    
    
l1 = [[1,2,3],[4,5,6]]
print(l1[0][2])


# slice example
print(spam[1:3])			# goes upto, but does not include, last item listed

print(len(spam))


print(list(range(0,100,2)))	# list() function creates a list with our range of items 0 to 100 in stepps of 2


a = 'aaa'
b = 'bbb'
a,b = b,a
print(a)
print(b)





