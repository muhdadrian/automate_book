# STEP 3: Join the Modified Lines

# the lines list now contains modified lines that start with stars.

# but, pyperclip.copy() is expecting a single str value, however, not a list of str values.

# to make this single str value, pass lines into the join() method to get a single str joined from the list's strs.
    

#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.


# text = [
#     'Lists of animals',
#     'Lists of aquarium life', 
#     'Lists of biologists by author abbreviation',
#     'Lists of cultivars',
# ]

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each str in "lines" list 

text = '\n'.join(lines)
pyperclip.copy(text)

# after running the code in terminal you command + V in the terminal also

