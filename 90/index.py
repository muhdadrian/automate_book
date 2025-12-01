# The append() method doesn't create a new list object; it changes the existing list object. 
# We call this "modifying the obj in-place".

eggs = ['cat', 'dog'] # this creates a new list
print(id(eggs))
eggs.append('moose') # append() modifies the list "in place".
print(id(eggs))
eggs = ['bat', 'rat', 'cow'] # this creates a new list, which has a new identity.
print(id(eggs)) # eggs now refers to a completely different list.

# if two vars refer to the same list and the list value itself changes, both vars are affected because they both refer to the same list.

# Python's automatic garbage collector deletes any values not being referred to by any vars to free up memory.