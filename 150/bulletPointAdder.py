# STEP 3: Join the Modified Lines

# the lines list now contains modified lines that start with stars.

# but, pyperclip.copy() is expecting a single str value, however, not a list of str values.

# to make this single str value, pass lines into the join() method to get a single str joined from the list's strs.


#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.


text = [
    "Lists of animals",
    "Lists of aquarium life",
    "Lists of biologists by author abbreviation",
    "Lists of cultivars",
]

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split("\n")
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[i] = "* " + lines[i]  # add star to each str in "lines" list

text = "\n".join(lines)
pyperclip.copy(text)

# after running the code in terminal:
#  you command + V in the terminal or in file.txt

# Get Text from Clipboard
# text = pyperclip.paste()
# This grabs whatever text you have copied right now.
# Example:
# If you copied 5 lines from a website → text now contains those 5 lines.

# lines = text.split("\n")
# This splits the big text into a Python list of lines.
# Example:
# "Apple\nBanana\nOrange"
# Becomes:
# ["Apple", "Banana", "Orange"]

# for i in range(len(lines)):
#     lines[i] = "* " + lines[i]
# This loop:
# Goes through each line by index
# Adds * in front
# Example:
# "Apple"  →  "* Apple"
# After the loop, your list becomes:
# ["* Apple", "* Banana", "* Orange"]

# Join the Lines Back Into One Text Block
# text = "\n".join(lines)
# This turns:
# ["* Apple", "* Banana", "* Orange"]
# Into:
# * Apple
# * Banana
# * Orange

# Copy the Final Result Back to Clipboard
# pyperclip.copy(text)

# Now the new formatted text is automatically:
# Back in your clipboard
# Ready to paste anywhere (Word, browser, WhatsApp, code, etc.)


# why this on the top: text = pyperclip.paste() instead of this: pyperclip.copy(text)
# Short Answer
# You use:
# text = pyperclip.paste()
# at the top because you need to GET text first
# and
# pyperclip.copy(text)
# at the bottom because you want to SEND text back to the clipboard after modifying it.

# So the flow is:
# PASTE (input) →  PROCESS →  COPY (output)


# Think of Clipboard Like a Photocopier
# Action:	                Code:	                What It Means:
# Take text from clipboard	pyperclip.paste()	    Read input
# Put text into clipboard	pyperclip.copy(text)	Send output


# Real-Life Analogy
# Imagine a printer/scanner machine:

# Real Life:	            Python Code:
# Scan paper	            paste()
# Edit on computer	        split(), for loop, join()
# Print the new version	    copy()
