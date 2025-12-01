# The in and not in Operators with Strings

# The in and not in operators can be used with strings just like with list values.

# An expression with two strings joined using in or not in will evaluate to a Boolean True or False.

print('Hello' in 'Hello, World')
print('Hello' in 'Hello')
print('HELLO' in 'Hello, World')
print('' in 'spam')
print('cats' not in 'cats and dogs')

# these expressions test whether the first string (the exact string, case-sensitive) can be found within the second string.