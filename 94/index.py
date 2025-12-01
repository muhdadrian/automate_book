# Dictionaries and Structuring Data 

# we assign dictionary to the myCat var:
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'} 

# the dictionary's keys: size, color, disposition
# the values for the keys: fat, gray and loud

# we can access the values through their keys:

print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.') 

# dictionaries can use int values as keys, just like lists use int for indexes, but do not have to start at 0 and can be any number

spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam)
print(spam[12345])
print(spam[42])