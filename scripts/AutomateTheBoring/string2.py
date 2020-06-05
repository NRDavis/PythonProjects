# string 2 -- string methods

'''
Notes:
strin methods are imutable, meaning we dont modify the original string, we return new strings


.upper()
.lower()

.isupper()
.islower()

.isalpha()          letters only
.isalnum()          letters and numbers only

.isdecimal()        numbers only 
.isspace()          whitespace only
.istitle()              titlecase only - all words in string start with capital letter and others are all lower case

.startswith()       return true if the string starts with an argument passed in
.endswith()

.join()                 passed list of strings and joins them together

.split()                we pass an argument, and it returns a list of strings split by that char, defaulted to whitespace chars

.ljust(X, fill)                return padded versions of strings (inserts X number of white space chars, alternaive fill chars)
.rjust(X, fill)

.strip()            # we strip off white space from a given segment of our string
.rstrip()
.lstrip()


pyperclip module allows us to copy and paste text from the command line





'''


spam = 'hello world'
print(spam.upper())
print(spam)

answer = input()
print(answer.upper())
print(answer.lower())


hello = 'hello'
a = hello.startswith('h')
print(a)


a = '\n\n'
b = ['abc', 'def', 'ghi']

a.join(b)
print(a.join(b))

consti = 'we the people, in order to form a more perfect union'
print(consti.split())

name = 'al'
print(name.center(20, '='))

bac = 'spamBaconspameggspam'
print(bac.strip('spam'))

