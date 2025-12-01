# Pretty Printing

# if you import the pprint module into your programs, you'll have access to the pprint() and pformat() functions that will "pretty print" a dictionary's values.

# this is helpful when you want a cleaner display of the items in a dictionary than what print() provides. 

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
# pprint.pprint(count)
# print(pprint.pformat(count))

# the output looks much cleaner with the keys sorted.

# the pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries.

# if you want to obtain the prettified text as a string value instead of displaying it on the screen, call pprint.pformat() instead.

# these two lines are equivalent to each other: 
# pprint.pprint(someDictonaryValue)
# print(pprint.pformat(someDictonaryValue))