# The keys(), values(), and items() Methods

# there are three dictionary methods that will return list-like values of the dictionary's keys, values, or both keys and values:
# 1. keys()
# 2. values()
# 3. items()

# the values returned by these methods are not true lists: they cannot be modified and do not have an append() method. 
# but these data types (dict_keys, dict_values, and dict_items, respectively) can be used in for loops.

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v) 

# a for loop iterates over each of the values in the spam dictionary.