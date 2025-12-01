# The setdefault() Method

# to set a value in a dictionary for a certain key if that key does not have a value.

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

print(spam)
