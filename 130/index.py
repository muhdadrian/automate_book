# The startswith() and endswith() Methods

# both methods above return True if the str value they are called on begins or ends (respectively) with the str passed to the method; otherwise, they return False.

# enter following into interactive shell:

print('Hello, world!'.startswith('Hello'))

print('Hello, world!'.endswith('world!'))

print('abc123'.startswith('abcdef'))

print('abc123'.endswith('12'))

print('Hello, world!'.startswith('Hello, world!'))

print('Hello, world!'.endswith('Hello, world!'))

# these methods are useful alternatives to the == equals operator if you need to check only whether the first or last part of the str, rather than the whole thing, is equal to another str.