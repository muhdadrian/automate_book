# Splitting Strings with the partition() Method

# this method split a str into the text before and after a separator str.

# it returns a tuple of three substrings for the "before," "separator," and "after" substrings.

print('Hello, world!'.partition('w'))

print('Hello, world!'.partition('world'))

# the method splits the str only on the first occurence:
print('Hello, world!'.partition('o'))

# if the separator str can't be found, the first str returned in the tuple will be the entire str, and the other two strs will be empty:
print('Hello, world!'.partition('XYZ'))