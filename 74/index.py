# sort() uses "ASCIIbetical order" rather than actual alphabetical order for sorting
# strings. This means uppercase letters come before lowercase letters.
# lowercase a is sorted so that it comes after the uppercase Z.

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
print(spam)
spam.sort()
print(spam) # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

# to sort the values in regular alphabetical order, pass str.lower for the key keyword arg in the sort() method call.

spam = ['a', 'z', 'A', 'Z']
print(spam) # to ease my restudy
spam.sort(key=str.lower)
print(spam) # ['a', 'A', 'z', 'Z']

# The sort() function treat all items in the list as if they were lowercase without actually changing the values in the list.