# Using random.choice() and random.shuffle() functions with lists

# random module has a couple functions that accept lists for arguments.
# random.choice() function will return a randomly selected item from the list.

import random

pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))

# you can consider random.choice(someList) to be a shorter form of
# someList[random.randint(0, len(someList) - 1]
