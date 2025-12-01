# Copying and Pasting Strings with the pyperclip Module

# the pyperclip module has copy() and paste() functions that can send text to and receive text from your computer's clipboard.

# sending the output of your program to the clipboard will make it easy to paste it into an email, word processor, or some other software.

# interactive shell:

import pyperclip

# print(pyperclip.copy('Hello, world!'))
print(pyperclip.copy('Hello, world!'))

print(pyperclip.paste()) # this is the result


# if something outside of your program changes the clipboard contents, the paste() function will return it.

# For example, if I copied this sentence to the clipboard and then called paste(), it would look like this:

print(pyperclip.paste())

# 'For example, if I copied this sentence to the clipboard and then called paste(), it would look like this:'