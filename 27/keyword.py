# print() function has the optional parameters end and sep to specify what should be
# printed at the end of its args and between its args (separating them), respectively.


print('Hello')
print('World')

# The output above is in separate outline, as the print() function automatically add a newline char
# to the end of the string.

print('Hello', end=' ')
print('World')
# You can set the end keyword arg to change the newline char to a different string.
# The output is printed on a single line because there is no longer a newline printed after 'Hello'.
# Instead, the blank string is printed. This is useful if you need to disable the newline that
# gets added to the end of every print() function call.
