import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')         # we put things inside 'groups' to make them callable by themselves
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))

# pipe characters           |


