# Step 3: Copy the Right Phrase

# the key phrase is stored as a str in the var keyphrase, you need to see whether it exists in the TEXT dictionary as a key.

# if so, you want to copy the key's value to the clipboard using pyperclip.copy().

# since you're using pyperclip module, you need to import it.

# you don't actually need the keyphrase var; you could just use sys.argv[1] everywhere keyphrase is used in this program.

# but, a var named keyphrase is much more readable than something cryptic like sys.argv[1]. 


#! python3
# mclip.py - A multi-clipboard program

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""
        }

import sys, pyperclip # import pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

# to check keyphrase in TEXT
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

# if the key phrase is a key in the dictionary, we get the value corresponding to that key, copy it to the clipboard, and print a msg saying that we copied the value.

# otherwise, we print a msg saying there's no key phrase with that name. 

# to run in the terminal: 
# python3 mclip.py agree
# python3 mclip.py busy
# python3 mclip.py upsell

# you will have to modify the TEXT dictionary value in the source whenever you want to update the program with a new msg.