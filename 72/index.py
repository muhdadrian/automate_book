# Sorting the Values in a List with the sort() Method

# Lists of number values and lists of strings can be sorted with the sort() method.

spam = [2, 5, 3.14, 1, -7]
print(spam)
spam.sort()
print(spam) # [-7, 1, 2, 3.14, 5]

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(spam)
spam.sort()
print(spam) # ['ants', 'badgers', 'cats', 'dogs', 'elephants']

# You can also pass True for the reverse keyword arg to have sort() sort the values in reverse order.

spam.sort(reverse=True)
print(spam) # ['elephants', 'dogs', 'cats', 'badgers', 'ants']