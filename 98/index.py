# dictionaries in Python 3.7 and later will remember the insertion order of their key-value pairs if you create a sequence value from them. 

# for e.g, the order of items in the lists made from eggs and ham dictionaries matches the order in which they were entered:

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
print(list(eggs)) # ['name', 'species', 'age']

ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(list(ham)) # ['species', 'age', 'name']

# the dictionaries are still unordered, as you can't access items in them using integer indexes like eggs[0] or ham[2].

# you shouldn't rely on this behaviour, as dictionaries in older versions of Python don't remember the insertion order of key-value pairs.

# for e.g, notice how the list doesn't match the insertion order of the dictionary's key-value pairs when I run this code in Python 3.5:

spam = {}
spam['first key'] = 'value'  
spam['second key'] = 'value'  
spam['third key'] = 'value'
print(list(spam)) # ['first key', 'third key', 'second key']   

