#!python3

import webbrowser,sys, pyperclip
if len(sys.argv) > 1:
    #Get address from the command line.
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
