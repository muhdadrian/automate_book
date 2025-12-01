# The first arg to insert() is the index for the new value, and the second arg is the new value to
# be inserted.

spam = ['cat', 'dog', 'bat']
print(spam)
spam.insert(1, 'chicken')
print(spam)

# Neither append() nor insert() gives the new value of spam as its return value. Infact, the return value of append() and insert() is None. You definitely, wouldn't want to store this as the new var value.

# The list is modified in place.