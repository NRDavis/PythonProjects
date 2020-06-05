'''
regular expressions

similar to find feature in most text editors

like a minilanguage to find text patterns --- worth it to avoid coding items ourself

'''
import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone 
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
        return False #missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
    
    
    
message = 'Call me 415-555-1011 tomorrow, or at 415-555-999'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phnoe number found: '+ chunk)
        foundNumber = True
    if not foundNumber:
        print('Could not find any phone number')
        
     
        
# Here, we're performing the same operation as the code above
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # allows use to search for this pattern
mo = phoneNumRegex.search(message)  # matched object
print(mo.group())


mo2 = phoneNumRegex.findall(message)
print(mo2)



