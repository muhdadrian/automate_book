# You can leave out one or both of the indexes on either side of the colon in the slice.
# Leaving out the first index is the same as using 0 / the beginning of of the list.
# Leaving out the second index is the same as using the length of the list, which will slice to the
# end of the list.

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])
print(spam[1:])
print(spam[:])