# The copy Module's copy() and deepcopy() Functions

# copy.copy() can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.

import copy
spam = ['A', 'B', 'C', 'D']
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese)) # cheese is a different list with different identity
cheese[1] = 42
print(spam) # ['A', 'B', 'C', 'D']
print(cheese) # ['A', 42, 'C', 'D']

# the spam and cheese vars refer to separate lists, which is why only the list in cheese is modified when you assign 42 at index 1.
# cheese = copy.copy(spam) creates a second list that can be modified independently of the 1st.
# if the list you need to copy contains lists, then use the copy.deepcopy() function.
# the deepcopy() function will copy these inner lists as well.