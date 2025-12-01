# Checking Whether a Key or Value Exists in a Dictionary

# in previous chapter, the in and not in operators can check whether a value exists in a list.

# you can also use those operators to see whether a certain key or value exists in a dictionary.

spam = {'name': 'Zophie', 'age': 7}

print('name' in spam.keys())
print('Zophie' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam)

# 'color' in spam is essentially a shorter version of writing 'color' in spam.keys().
# if you ever want to check whether a value is (or isn't) a key in the dictionary, you can simply use the in (or not in) keyword with the dictionary value itself.


