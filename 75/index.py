# Reversing the Values in a List with the reverse() Method

spam = ['cat', 'dog', 'moose']
print(spam) # to ease restudy
spam.reverse()
print(spam) # ['moose', 'dog', 'cat']

# Like sort() list method, reverse() doesn't return a list. This is why you write spam.reverse(),
# instead of spam = spam.reverse().

# The trick below is useful when you want to rearrange long lines of Python code to be a bit more
# readable:
print('Four score and seven ' + \
      'years ago...')