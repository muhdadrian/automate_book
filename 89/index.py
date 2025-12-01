# strs are immutable and cannot be changed. 
# If you "change" the str in a var, a new str obj is being made at a different place in memory, and the var refers to this new str.

bacon = 'Hello'
print(bacon)
print(id(bacon))
bacon += ' world!'
print(bacon)
print(id(bacon))
