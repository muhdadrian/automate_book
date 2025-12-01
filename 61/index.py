# The random.shuffle() function will reorder the items in a list. This function modifies
# the list in place, rather than returning a new list.

import random

people = ['Alice', 'Bob', 'Carol', 'David']
print(people) # to ease my restudy
print('\n') # to ease my restudy

random.shuffle(people)
print(people)
random.shuffle(people)
print(people)
