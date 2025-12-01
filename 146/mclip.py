# Project: Multi-Clipboard Automatic Messages

# If you've responded to a large number of emails with similar phrasing, you've probably had to do a lot of repetitive typing.

# Maybe you keep a text document with these phrases so you can easily copy and paste them using the clipboard. 

# But, your clipboard can only store one message at a time, which isn't very convenient.

# Let's make this process a bit easier with a program that stores multiple phrases.


# Step 1: Program Design and Data Structures

# you need to start the program with a #! (shebang) line and write a comment briefly describes the program.


#! python3
# mclip.py - A multi-clipboard program

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""
        }

# Step 2: Handle Command Line Arguments 

# the command line args will be stored in the var sys.arg.

# the first item in the sys.argv list should always be a str containing the program's filename ('myclip.py'),

# the second item should be the first command line arg.

# for this program, this arg is the key phrase of the msg you want.

# command line arg is mandatory, you display a usage to the user if they forget to add it (that is, if the sys.argv list has fewer than two values in it).

import sys

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

# Step 3, go to 147