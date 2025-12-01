# Indexing and Slicing Strings

# strings use indexes and slices the same way lists do.
# you can think of the string 'Hello, world!' as a list and each character in the string as an item with a corresponding index.

# ' H e l l o ,   w o r l  d  ! '
#   0 1 2 3 4 5 6 7 8 9 10 11 12

# The space and exclamation point are included in the character count, so 'Hello, world!' is 13 characters long, from H at index 0 to ! at index 12.

spam = 'Hello, world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[7:])

# if you specify an index, you'll get the character at that position in the string.
# if you specify a range from one index to another, the starting index is included and the ending index is not.
# the substring you get from spam[0:5] will include everything from spam[0] to spam[4], leaving out the comma at index 5 and the space at index 6. This is similar to how range(5) will cause a for loop to iterate up to, but not including 5.
# slicing a string does not modify the original string. 