# dictionaries are unordered, unlike lists.

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

# because dictionaries are not ordered, they can't be sliced like lists.