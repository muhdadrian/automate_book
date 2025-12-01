# STEP 2: Separate the Lines of Text and Add the Star 


#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each str in "lines" list 

pyperclip.copy(text)

# we split the text along its newlines to get a list in which each item is one line of the text.

# we store the list in lines and then loop through the items in lines.

# For each line, we add a star and a space to the start of the line. 

# Now each str in lines begins with a star.

# Step 3: Go to 150