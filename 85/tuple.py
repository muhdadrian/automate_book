# Converting Types with the list() and tuple() Functions

# Just like how str(42) will return '42', the str representation of the int 42, the functions list() and tuple() will return list and tuple versions of the values passed to them.

print(tuple(['cat', 'dog', 5])) # ('cat', 'dog', 5)
print(list(('cat', 'dog', 5))) # ['cat', 'dog', 5]
print(list('hello')) # ['h', 'e', 'l', 'l', 'o']

# converting a tuple to a list is handy if you need a mutable version of a tuple value.
