'''
Spongebob text:
	For when typing correctly just wont do.
'''

def sponge(text, output):
    #print("Length of our input string: "+str(len(text)))
    for i in range(0, len(text)):
        if i %2 == 1:
            output.append(text[i].upper())
            #output = output + text[i].upper()
            #text[i] = text[i].upper()
        else:
            output.append(text[i].lower())
            #output = output + text[i].lower()
            #text[i] = text[i].lower()
	
    output = str(''.join(output))
        
		
			
test_string = "does this Work?"
output = []


#for i in range(0,15):
#    print(test_string[i])


sponge(test_string, output)
print( ''.join(output))
#print(output)
