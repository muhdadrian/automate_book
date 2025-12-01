# The get() method

# it's tedious to check whether a key exists in a dictionary before accessing that key's value.
# dictionaries have a get() method that takes two args:
# 1. the key of the value to retrieve 
# 2. a fallback value to return if that key does not exist.

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# because there is no 'eggs' key in the picnicItems dictionary, the default value 0 is returned by the get() method.







