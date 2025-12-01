# a common use of split() is to split a multiline str along the newline chars.

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))

# passing split() the arg '\n' lets us split the multiline str stored in spam along the newlines and return a list in which each item corresponds to one line of the str.