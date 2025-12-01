# Methods belong to a single data type. 

# The append() and insert() methods are list methods and can be called only on list values, not on other values such as strings or integers

eggs = 'hello'
eggs.append('world')
print(eggs) # This will produce error

bacon = 42
bacon.insert(1, 'world')
print(bacon) # This will produce error
