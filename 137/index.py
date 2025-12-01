# Justifying Text with the rjust(), ljust(), and center() Methods

# the rjust() and ljust() str methods return a padded version of the str they are called on, with spaces inserted to justify the text.

# the first arg to both methods is an int length for the justified str.

print('Hello'.rjust(10))

# 'Hello'.rjust(10) says that we want to right-justify 'Hello' in a str of total length 10.

# 'Hello' is five chars, so five spaces will be added to its left, giving us a str of 10 chars with 'Hello' justified right 

print('Hello'.rjust(20))

print('Hello, World'.rjust(20))

print('Hello'.ljust(10))