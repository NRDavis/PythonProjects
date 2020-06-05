# example code given within automate the boring stuff text
import pprint
'''
triple quotes are actually giant string --- multilined string

'''
message = 'It was a bright cold day in April, and the clock...'
count = {}		# initialize dictionary

# we use string method upper to ensure that we're not differentiating between letter case
for character in message.upper():
	count.setdefault(character, 0)	# we set each character's count to zero to start off
	count[character] = count[character] + 1

pprint.pprint(count)		# we print our dictionary, with each of the occurences of the characters displayed



# get method can return default value if one does not exist