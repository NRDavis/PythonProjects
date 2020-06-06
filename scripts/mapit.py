'''
This script allows you to launch a google maps search from the command line

using ubuntu, enter:

$ python3 mapit.py full-address-here

'''

import webbrowser, sys, pyperclip

sys.argv # [mapit.py, '870', Valencia', 'st.']

# check if command line arguments were passed
if len(sys.argv) > 1:           # check number of command line arguments
    # we need to combine all comand line arguments into a single strign
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    # takes item from the clipboard and pastes it to our address object

#    https://www.google.com/maps/place/<ADDRESS>
webbrowser.open("https://www.google.com/maps/place/"+address)