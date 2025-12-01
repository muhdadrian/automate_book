# The proper way to "mutate" a str is to use slicing and concatenation to build a new str by copying from parts of the old str.

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name) # Zophie a cat
print(newName) # Zophie the cat

# The original 'Zophie a cat' str is not modified, because strs are immutable.