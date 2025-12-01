# Three things to note about the sort() method:

# 1st, sort() method sorts the list in place; don't try to capture the return value by writing code like spam = spam.sort().
# 2nd, you cannot sort lists that have both number values and string values in them, since Python doesn't know how to compare these values.

spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
print(spam) # This will output error

# 3rd in 74