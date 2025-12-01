spam = {'color': 'red', 'age': 42}
print(spam.keys())
print(list(spam.keys()))

# the list(spam.keys()) line takes the dict_keys value returned from keys() and passes it to list(), which then returns a list value of ['color', 'age']