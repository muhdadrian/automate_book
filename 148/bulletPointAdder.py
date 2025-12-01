# Project: Adding Bullets to Wiki Markup

# when editing a Wikipedia article, you can create a bulleted list by putting each list item on its own line and placing a star in front.

# but you have a really large list that you want to add bullet points to.

# you could just type those stars at the beginning of each line, one by one. Or you could automate this task with a short Python script.

# our script (bulletPointAdder.py) will get the text from the clipboard, add a star and space to the beginning of each line, and then paste this new text to the clipboard.

# for e.g, we copied the following Wikipedia text of "List of Lists of Lists" to the clipboard: 

# Lists of animals
# Lists of aquarium life 
# Lists of biologists by author abbreviation
# Lists of cultivars

# when we run our script, the clipboard would then contain:

# * Lists of animals
# * Lists of aquarium life 
# * Lists of biologists by author abbreviation
# * Lists of cultivars

# this star-prefixed text is ready to be pasted into a Wikipedia article as a bulleted list.


# Step 1: Copy and Paste from the Clipboard

# you want your script to do the following:
# 1. Paste text from the clipboard.
# 2. Do something to it.
# 3. Copy the new text to the clipboard

# the second step is a little tricky, but steps 1 and 3 are pretty straighforward: they just involve the pyperclip.copy() and pyperclip.paste() functions.

# let's just write the part of the program that covers steps 1 and 3.


#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars

pyperclip.copy(text)

# TODO comment is a reminder that you should complete this part of the program.

# STEP 2: Go to 149