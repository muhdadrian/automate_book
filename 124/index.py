# Useful String Methods

# upper()
# lower()
# isupper()
# islower()

# the upper() and lower() string methods return a new string where all the letters in the original string have been converted to uppercase or lowercase, respectively.

# nonletter characters in the string remain unchanged. Enter the following into the interactive shell:

spam = 'Hello, world!'
spam = spam.upper()
print(spam)

spam = spam.lower()
print(spam)

# these methods do not change the string itself but return new string values.

# to change the original string, you have to call upper() or lower() on the string and then assign the new string to the variable where the original was stored.

# you must use spam = spam.upper() to change the string in spam instead of simply spam.upper().

# this is just like if a var eggs contains the value 10. Writing eggs + 3 does not change the value of eggs, but eggs = eggs + 3 does.